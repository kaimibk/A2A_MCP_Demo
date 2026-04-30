from dataclasses import dataclass
from datetime import datetime

from fastmcp import FastMCP

# Initialize the FastMCP app
mcp = FastMCP("mcp-orders")


# Define data models
@dataclass
class Order:
    item: str
    status: str
    date: datetime


# Load "database"
# This is a simple in-memory database for demonstration purposes. In a real application, this would be replaced with a proper database connection.
DB = {
    "123": Order(item="Laptop", status="Delivered", date=datetime(2026, 4, 20)),
    "456": Order(item="Smartphone", status="Shipped", date=datetime(2026, 4, 22)),
    "789": Order(item="Headphones", status="Processing", date=datetime(2026, 4, 25)),
}


@mcp.tool()
def get_order(order_id: str) -> Order:
    """Fetch order details by ID."""
    order_data = DB.get(order_id, None)

    if order_data is None:
        raise ValueError(f"Order with ID {order_id} not found.")

    return order_data


@mcp.tool()
def today_datetime() -> datetime:
    """Get today's date"""
    return datetime.today()


if __name__ == "__main__":
    # Run the FastMCP app
    mcp.run(transport="http", host="0.0.0.0", port=8000)
