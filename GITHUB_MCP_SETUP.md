# GitHub MCP Server Setup Guide

This guide will help you set up the GitHub MCP (Model Context Protocol) server for your matrix multiplication project.

## 🔧 Prerequisites

- Node.js and npm installed
- A GitHub account
- A GitHub Personal Access Token

## 📋 Setup Steps

### 1. Create a GitHub Personal Access Token

1. Go to GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name like "MCP Server Token"
4. Select the following scopes:
   - `repo` (Full control of private repositories)
   - `read:org` (Read org and team membership)
   - `read:user` (Read user profile data)
   - `user:email` (Access user email addresses)

### 2. Configure the MCP Server

#### Option A: Update Global MCP Configuration
Edit your global MCP configuration file at `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_github_token_here"
      }
    }
  }
}
```

#### Option B: Use Local Configuration
1. Copy the provided `mcp.json` file to your Cursor settings
2. Replace `"GITHUB_PERSONAL_ACCESS_TOKEN": ""` with your actual token

### 3. Environment Variables (Recommended)

For security, it's better to use environment variables:

1. Create a `.env` file in your project root:
```bash
GITHUB_PERSONAL_ACCESS_TOKEN=your_github_token_here
```

2. Update your MCP configuration to reference the environment variable:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

3. Add `.env` to your `.gitignore` file to avoid committing sensitive data

### 4. Test the Configuration

1. Restart Cursor
2. Try using GitHub-related commands in the chat
3. The MCP server should automatically install when first used

## 🚀 Available Features

Once configured, you can use the GitHub MCP server to:

- **Repository Management**: Create, read, and manage repositories
- **Issue Management**: Create, update, and search issues
- **Pull Request Operations**: Create and manage pull requests
- **File Operations**: Read, create, and modify files in repositories
- **Branch Management**: Create and switch branches
- **Search Capabilities**: Search repositories, code, issues, and users

## 💡 Usage Examples

With the GitHub MCP server configured, you can ask Cursor to:

```
"Create a new repository for this matrix multiplication project"
"Create an issue for adding performance optimizations"
"Search for similar matrix multiplication projects on GitHub"
"Create a pull request with the latest changes"
```

## 🔒 Security Best Practices

1. **Never commit tokens**: Always use environment variables or secure storage
2. **Minimal permissions**: Only grant necessary scopes to your token
3. **Regular rotation**: Rotate your tokens periodically
4. **Monitor usage**: Check your token usage in GitHub settings

## 🐛 Troubleshooting

### Common Issues

**"GitHub token not found"**
- Verify your token is correctly set in the environment variable
- Check that the token has the required scopes

**"MCP server failed to start"**
- Ensure Node.js is installed: `node --version`
- Try manually installing: `npm install -g @modelcontextprotocol/server-github`

**"Permission denied"**
- Verify your token has the correct scopes
- Check if the repository exists and you have access

### Debug Steps

1. Check Cursor's developer console for error messages
2. Verify your token works with GitHub API:
   ```bash
   curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user
   ```
3. Test the MCP server directly if needed

## 📚 Additional Resources

- [GitHub MCP Server Documentation](https://github.com/modelcontextprotocol/servers/tree/main/src/github)
- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io/)
- [GitHub API Documentation](https://docs.github.com/en/rest)

---

**Note**: This setup enables powerful GitHub integration capabilities within Cursor using the Model Context Protocol.