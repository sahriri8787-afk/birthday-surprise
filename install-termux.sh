#!/data/data/com.termux/files/usr/bin/bash
set -e
TARGET="$HOME/birthday-surprise"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
rm -rf "$TARGET"
mkdir -p "$TARGET"
cp -r "$SCRIPT_DIR"/* "$TARGET"/
mkdir -p "$TARGET/assets/confetti"
chmod +x "$TARGET/install-termux.sh" 2>/dev/null || true
cat > "$TARGET/start.sh" <<'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd "$HOME/birthday-surprise"
echo "Birthday Surprise: http://127.0.0.1:8080"
python -m http.server 8080 --bind 127.0.0.1
EOF
chmod +x "$TARGET/start.sh"
echo "نصب با موفقیت انجام شد."
echo "اجرا: bash ~/birthday-surprise/start.sh"
