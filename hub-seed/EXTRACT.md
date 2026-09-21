# Extract this into its own repository

This directory is the hub, staged here only because the integration that wrote it cannot create
repositories. It does not belong in cipher-lab. Move it out, then delete it from here.

```bash
# 1. create the repo (any name; "hub" is just a default)
gh repo create NoAutopilot/hub --private

# 2. move the contents into it
git clone https://github.com/NoAutopilot/hub.git ~/src/hub
cp -r ~/src/cipher-lab/hub-seed/. ~/src/hub/
rm ~/src/hub/EXTRACT.md
cd ~/src/hub && git add -A && git commit -m "Hub: registry, conventions, bootstrap brief, estate CLI" && git push

# 3. point the shell tools at your checkouts
cp shell/projects.conf.example shell/projects.conf
$EDITOR shell/projects.conf
echo 'source ~/src/hub/shell/projects.sh' >> ~/.zshrc   # or ~/.bashrc

# 4. take it out of cipher-lab
cd ~/src/cipher-lab && git rm -r hub-seed && git commit -m "Hub extracted to its own repository" && git push
```

Then `estate` shows every project, `asks` shows everything blocked on a human across all of them,
`go CIPHER-LAB` pulls and drops you into a current session, and `hubnew "reselling Lego"` runs the
bootstrap brief.
