#!/bin/bash

# Set the install path (default: /usr/local/bin)
INSTALL_PATH="/usr/local/bin/wc_tool"

# Create the shell wrapper
echo '#!/bin/bash' | sudo tee $INSTALL_PATH > /dev/null
echo "docker run --rm <your-username>/wc_tool \"\$@\"" | sudo tee -a $INSTALL_PATH > /dev/null

# Make it executable
sudo chmod +x $INSTALL_PATH

echo "✅ wc_tool installed! Run it using: wc_tool 'a'"


curl -fsSL https://raw.githubusercontent.com/<your-username>/wc_tool/main/install_wc_tool.sh | bash

