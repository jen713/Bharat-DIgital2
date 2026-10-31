from fastmcp import FastMCP

mcp = FastMCP("Citizen MCP")

APPLICATIONS = {}

@mcp.tool()
def check_application_status(
    application_id: int
):
    """
    Check pension application status
    """

    return {
        "application_id": application_id,
        "status": "PENDING"
    }

if __name__ == "__main__":
    mcp.run()
