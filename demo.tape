# VHS demo: Installing overheid-plugins marketplace
# Run with: vhs demo.tape

Output demo.gif

Set Shell "zsh"
Set FontSize 16
Set Width 900
Set Height 500
Set Theme "Catppuccin Mocha"
Set TypingSpeed 50ms
Set Padding 20

# Title
Type "# Overheid Claude Plugins - Marketplace"
Enter
Sleep 1s

# Step 1: Add the marketplace
Type "claude plugin marketplace add developer-overheid-nl/overheid-claude-plugins"
Enter
Sleep 3s

# Step 2: Show available marketplaces
Type "claude plugin marketplace list"
Enter
Sleep 3s

# Step 3: Install a plugin
Type "claude plugin install developer-overheid@overheid-plugins"
Enter
Sleep 3s

# Step 4: Show installed plugins
Type "claude plugin list"
Enter
Sleep 5s
