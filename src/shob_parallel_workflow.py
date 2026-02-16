from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class OrderState(TypedDict):
    orderId: int
    inventory_check: str
    payment_processing: str
    delivery_estimate: str
    order_status: str


def estimate_delivery(state: OrderState):
    return {"delivery_estimate":"delivery_date_fixed"}

def process_payment(state: OrderState):
    return {"payment_processing":"payment_not_done"}

def check_invetory(state: OrderState):
    return {"inventory_check":"item_available"}

def order_status(state: OrderState):
    return {"order_status":"failed"}

def pwf(order_Id: int):
    #creating graph
    graph = StateGraph(OrderState)

    #adding node
    graph.add_node('estimate_delivery', estimate_delivery)
    graph.add_node('process_payment', process_payment)
    graph.add_node('check_invetory', check_invetory)

    graph.add_node('order_status', order_status)

    #adding edges
    graph.add_edge(START, 'estimate_delivery')
    graph.add_edge(START, 'process_payment')
    graph.add_edge(START, 'check_invetory')

    graph.add_edge('estimate_delivery', 'order_status')
    graph.add_edge('process_payment', 'order_status')
    graph.add_edge('check_invetory', 'order_status')

    graph.add_edge('order_status', END)

    return graph.compile().invoke({'orderId':order_Id })