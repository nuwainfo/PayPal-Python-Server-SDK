# Orders

Use the `/orders` resource to create, update, retrieve, authorize, capture and track orders.

```python
orders_controller = client.orders
```

## Class Name

`OrdersController`

## Methods

* [Create Order](../../doc/controllers/orders.md#create-order)
* [Get Order](../../doc/controllers/orders.md#get-order)
* [Patch Order](../../doc/controllers/orders.md#patch-order)
* [Confirm Order](../../doc/controllers/orders.md#confirm-order)
* [Authorize Order](../../doc/controllers/orders.md#authorize-order)
* [Capture Order](../../doc/controllers/orders.md#capture-order)
* [Create Order Tracking](../../doc/controllers/orders.md#create-order-tracking)
* [Update Order Tracking](../../doc/controllers/orders.md#update-order-tracking)


# Create Order

Creates an order. Merchants and partners can add Level 2 and 3 data to payments to reduce risk and payment processing costs. For more information about processing payments, see checkout or multiparty checkout. Note: For error handling and troubleshooting, see Orders v2 errors.

```python
def create_order(self,
                options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`OrderRequest`](../../doc/models/order-request.md) | Body, Required | - |
| `paypal_mock_response` | `str` | Header, Optional | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant. |
| `paypal_request_id` | `str` | Header, Optional | The server stores keys for 6 hours. The API callers can request the times to up to 72 hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g. Create Order Request with payment source information like Card, PayPal.vault_id, PayPal.billing_agreement_id, etc).<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `108` |
| `paypal_partner_attribution_id` | `str` | Header, Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36` |
| `paypal_client_metadata_id` | `str` | Header, Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36` |
| `prefer` | `str` | Header, Optional | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: `'return=minimal'`<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `25`, *Pattern*: `^[a-zA-Z=,-]*$` |
| `paypal_auth_assertion` | `str` | Header, Optional | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Order`](../../doc/models/order.md).

## Example Usage

```python
collect = {
    'body': OrderRequest(
        intent=CheckoutPaymentIntent.CAPTURE,
        purchase_units=[
            PurchaseUnitRequest(
                amount=AmountWithBreakdown(
                    currency_code='currency_code6',
                    value='value0'
                )
            )
        ]
    ),
    'prefer': 'return=minimal'
}
result = orders_controller.create_order(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Request is not well-formed, syntactically incorrect, or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 401 | Authentication failed due to missing authorization header, or invalid authentication credentials. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The requested action could not be performed, semantically incorrect, or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Order

Shows details for an order, by ID. Note: For error handling and troubleshooting, see Orders v2 errors.

```python
def get_order(self,
             options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of the order for which to show details.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36`, *Pattern*: `^[A-Z0-9]+$` |
| `paypal_mock_response` | `str` | Header, Optional | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant. |
| `paypal_auth_assertion` | `str` | Header, Optional | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion. |
| `fields` | `str` | Query, Optional | A comma-separated list of fields that should be returned for the order. Valid filter field is `payment_source`.<br>**Constraints**: *Pattern*: `^[a-z_]*$` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Order`](../../doc/models/order.md).

## Example Usage

```python
collect = {
    'id': 'id0'
}
result = orders_controller.get_order(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Authentication failed due to missing authorization header, or invalid authentication credentials. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The specified resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |


# Patch Order

Updates an order with a `CREATED` or `APPROVED` status. You cannot update an order with the `COMPLETED` status. To make an update, you must provide a `reference_id`. If you omit this value with an order that contains only one purchase unit, PayPal sets the value to `default` which enables you to use the path: \"/purchase_units/@reference_id=='default'/{attribute-or-object}\". Merchants and partners can add Level 2 and 3 data to payments to reduce risk and payment processing costs. For more information about processing payments, see checkout or multiparty checkout. Note: For error handling and troubleshooting, see Orders v2 errors. Patchable attributes or objects: Attribute Op Notes intent replace payer replace, add Using replace op for payer will replace the whole payer object with the value sent in request. purchase_units replace, add purchase_units[].custom_id replace, add, remove purchase_units[].description replace, add, remove purchase_units[].payee.email replace purchase_units[].shipping.name replace, add purchase_units[].shipping.email_address replace, add purchase_units[].shipping.phone_number replace, add purchase_units[].shipping.options replace, add purchase_units[].shipping.address replace, add purchase_units[].shipping.type replace, add purchase_units[].soft_descriptor replace, remove purchase_units[].amount replace purchase_units[].items replace, add, remove purchase_units[].invoice_id replace, add, remove purchase_units[].payment_instruction replace purchase_units[].payment_instruction.disbursement_mode replace By default, disbursement_mode is INSTANT. purchase_units[].payment_instruction.payee_receivable_fx_rate_id replace, add, remove purchase_units[].payment_instruction.platform_fees replace, add, remove purchase_units[].supplementary_data.airline replace, add, remove purchase_units[].supplementary_data.card replace, add, remove application_context.client_configuration replace, add

```python
def patch_order(self,
               options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of the order to update.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36`, *Pattern*: `^[A-Z0-9]+$` |
| `paypal_mock_response` | `str` | Header, Optional | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant. |
| `paypal_auth_assertion` | `str` | Header, Optional | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion. |
| `body` | [`List[Patch]`](../../doc/models/patch.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
collect = {
    'id': 'id0',
    'body': [
        Patch(
            op=PatchOp.ADD
        )
    ]
}
result = orders_controller.patch_order(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Request is not well-formed, syntactically incorrect, or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 401 | Authentication failed due to missing authorization header, or invalid authentication credentials. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The specified resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The requested action could not be performed, semantically incorrect, or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |


# Confirm Order

Payer confirms their intent to pay for the the Order with the given payment source.

```python
def confirm_order(self,
                 options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of the order for which the payer confirms their intent to pay.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36`, *Pattern*: `^[A-Z0-9]+$` |
| `paypal_client_metadata_id` | `str` | Header, Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36` |
| `paypal_auth_assertion` | `str` | Header, Optional | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion. |
| `prefer` | `str` | Header, Optional | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: `'return=minimal'`<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `25`, *Pattern*: `^[a-zA-Z=]*$` |
| `body` | [`ConfirmOrderRequest`](../../doc/models/confirm-order-request.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Order`](../../doc/models/order.md).

## Example Usage

```python
collect = {
    'id': 'id0',
    'prefer': 'return=minimal'
}
result = orders_controller.confirm_order(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Request is not well-formed, syntactically incorrect, or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | Authorization failed due to insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The requested action could not be performed, semantically incorrect, or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | An internal server error has occurred. | [`ErrorException`](../../doc/models/error-exception.md) |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |


# Authorize Order

Authorizes payment for an order. To successfully authorize payment for an order, the buyer must first approve the order or a valid payment_source must be provided in the request. A buyer can approve the order upon being redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response. Note: For error handling and troubleshooting, see Orders v2 errors.

```python
def authorize_order(self,
                   options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of the order for which to authorize.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36`, *Pattern*: `^[A-Z0-9]+$` |
| `paypal_mock_response` | `str` | Header, Optional | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant. |
| `paypal_request_id` | `str` | Header, Optional | The server stores keys for 6 hours. The API callers can request the times to up to 72 hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g. Create Order Request with payment source information like Card, PayPal.vault_id, PayPal.billing_agreement_id, etc).<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `108` |
| `prefer` | `str` | Header, Optional | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: `'return=minimal'`<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `25`, *Pattern*: `^[a-zA-Z=,-]*$` |
| `paypal_client_metadata_id` | `str` | Header, Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36` |
| `paypal_auth_assertion` | `str` | Header, Optional | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion. |
| `body` | [`OrderAuthorizeRequest`](../../doc/models/order-authorize-request.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrderAuthorizeResponse`](../../doc/models/order-authorize-response.md).

## Example Usage

```python
collect = {
    'id': 'id0',
    'prefer': 'return=minimal'
}
result = orders_controller.authorize_order(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Request is not well-formed, syntactically incorrect, or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 401 | Authentication failed due to missing authorization header, or invalid authentication credentials. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | The authorized payment failed due to insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The specified resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The requested action could not be performed, semantically incorrect, or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | An internal server error has occurred. | [`ErrorException`](../../doc/models/error-exception.md) |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |


# Capture Order

Captures payment for an order. To successfully capture payment for an order, the buyer must first approve the order or a valid payment_source must be provided in the request. A buyer can approve the order upon being redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response. Note: For error handling and troubleshooting, see Orders v2 errors.

```python
def capture_order(self,
                 options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of the order for which to capture a payment.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36`, *Pattern*: `^[A-Z0-9]+$` |
| `paypal_mock_response` | `str` | Header, Optional | PayPal's REST API uses a request header to invoke negative testing in the sandbox. This header configures the sandbox into a negative testing state for transactions that include the merchant. |
| `paypal_request_id` | `str` | Header, Optional | The server stores keys for 6 hours. The API callers can request the times to up to 72 hours by speaking to their Account Manager. It is mandatory for all single-step create order calls (E.g. Create Order Request with payment source information like Card, PayPal.vault_id, PayPal.billing_agreement_id, etc).<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `108` |
| `prefer` | `str` | Header, Optional | The preferred server response upon successful completion of the request. Value is: return=minimal. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the id, status and HATEOAS links. return=representation. The server returns a complete resource representation, including the current state of the resource.<br>**Default**: `'return=minimal'`<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `25`, *Pattern*: `^[a-zA-Z=,-]*$` |
| `paypal_client_metadata_id` | `str` | Header, Optional | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36` |
| `paypal_auth_assertion` | `str` | Header, Optional | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion. |
| `body` | [`OrderCaptureRequest`](../../doc/models/order-capture-request.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Order`](../../doc/models/order.md).

## Example Usage

```python
collect = {
    'id': 'id0',
    'prefer': 'return=minimal'
}
result = orders_controller.capture_order(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Request is not well-formed, syntactically incorrect, or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 401 | Authentication failed due to missing authorization header, or invalid authentication credentials. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | The authorized payment failed due to insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The specified resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The requested action could not be performed, semantically incorrect, or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | An internal server error has occurred. | [`ErrorException`](../../doc/models/error-exception.md) |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |


# Create Order Tracking

Adds tracking information for an Order.

```python
def create_order_tracking(self,
                         options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of the order that the tracking information is associated with.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36`, *Pattern*: `^[A-Z0-9]+$` |
| `body` | [`OrderTrackerRequest`](../../doc/models/order-tracker-request.md) | Body, Required | - |
| `paypal_auth_assertion` | `str` | Header, Optional | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Order`](../../doc/models/order.md).

## Example Usage

```python
collect = {
    'id': 'id0',
    'body': OrderTrackerRequest(
        capture_id='capture_id8',
        notify_payer=False
    )
}
result = orders_controller.create_order_tracking(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Request is not well-formed, syntactically incorrect, or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | Authorization failed due to insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The specified resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The requested action could not be performed, semantically incorrect, or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | An internal server error has occurred. | [`ErrorException`](../../doc/models/error-exception.md) |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |


# Update Order Tracking

Updates or cancels the tracking information for a PayPal order, by ID. Updatable attributes or objects: Attribute Op Notes items replace Using replace op for items will replace the entire items object with the value sent in request. notify_payer replace, add status replace Only patching status to CANCELLED is currently supported.

```python
def update_order_tracking(self,
                         options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of the order that the tracking information is associated with.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36`, *Pattern*: `^[A-Z0-9]+$` |
| `tracker_id` | `str` | Template, Required | The order tracking ID.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36`, *Pattern*: `^[A-Z0-9]+$` |
| `paypal_auth_assertion` | `str` | Header, Optional | An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see PayPal-Auth-Assertion. |
| `body` | [`List[Patch]`](../../doc/models/patch.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
collect = {
    'id': 'id0',
    'tracker_id': 'tracker_id2',
    'body': [
        Patch(
            op=PatchOp.ADD
        )
    ]
}
result = orders_controller.update_order_tracking(collect)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Request is not well-formed, syntactically incorrect, or violates schema. | [`ErrorException`](../../doc/models/error-exception.md) |
| 403 | Authorization failed due to insufficient permissions. | [`ErrorException`](../../doc/models/error-exception.md) |
| 404 | The specified resource does not exist. | [`ErrorException`](../../doc/models/error-exception.md) |
| 422 | The requested action could not be performed, semantically incorrect, or failed business validation. | [`ErrorException`](../../doc/models/error-exception.md) |
| 500 | An internal server error has occurred. | [`ErrorException`](../../doc/models/error-exception.md) |
| Default | The error response. | [`ErrorException`](../../doc/models/error-exception.md) |

