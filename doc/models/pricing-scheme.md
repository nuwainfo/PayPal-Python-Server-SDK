
# Pricing Scheme

The pricing scheme details.

## Structure

`PricingScheme`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |
| `pricing_model` | [`PricingModel`](../../doc/models/pricing-model.md) | Required | The pricing model for the billing cycle.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `24`, *Pattern*: `^[A-Z_]+$` |
| `reload_threshold_amount` | [`Money`](../../doc/models/money.md) | Optional | The currency and amount for a financial transaction, such as a balance or payment due. |

## Example (as JSON)

```json
{
  "price": {
    "currency_code": "currency_code8",
    "value": "value4"
  },
  "pricing_model": "FIXED",
  "reload_threshold_amount": {
    "currency_code": "currency_code0",
    "value": "value6"
  }
}
```

