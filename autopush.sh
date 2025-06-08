#!/bin/bash

# Couleurs
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}--- ShadowMerge+ AutoPush ---${NC}"

# Vérifie que le dossier est bien un repo Git
if [ ! -d ".git" ]; then
    echo "Ce dossier n'est pas initialisé avec Git. Lancement de git init..."
    git init
fi

# Vérifie que le remote est bien configuré
remote_url=$(git remote get-url origin 2>/dev/null)
if [[ "$remote_url" != "https://github.com/237-Arcan/ShadowMergePlus.git" ]]; then
    echo "Configuration ou correction du remote origin..."
    git remote remove origin 2>/dev/null
    git remote add origin https://github.com/237-Arcan/ShadowMergePlus.git
fi

# Ajout des fichiers
git add .

# Commit avec message automatique horodaté
commit_message="AutoPush: $(date +'%Y-%m-%d %H:%M:%S')"
git commit -m "$commit_message"

# Push vers le dépôt
git push -u origin main

echo -e "${GREEN}✅ Push terminé avec succès.${NC}"
