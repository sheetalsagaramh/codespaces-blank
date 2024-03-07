from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

# Azure DevOps organization URL
organization_url = "https://dev.azure.com/your_organization"

# Personal access token (PAT) with appropriate permissions
personal_access_token = "your_personal_access_token"

# Create a connection to Azure DevOps
credentials = BasicAuthentication("", personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client for Azure Repos
repos_client = connection.clients.get_git_client()

# Now you can use the repos_client to perform various operations on your Azure Repos
# For example, you can get a list of repositories:
repositories = repos_client.get_repositories()

for repository in repositories:
    print(repository.name)
