from before_strategy.order import Order
from before_strategy.shipper import Shipper
from before_strategy.shipping_cost import ShippingCost

# Test Fereral ecpress shipping

order = Order(Shipper.fedex)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

#Test UPS shipping

order = Order(Shipper.ups)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

#Test postal service shipping

order = Order(Shipper.postal)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0

print("Tets pass")