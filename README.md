# 🛠️ Warehouse

![Image banner in the style of GNOME art showing a box truck, tower crane, and storage garage sat on and next to a road.](readme_banner.svg)

## Warehouse est une boîte à outils polyvalente pour gérer les données de l'utilisateur flatpak, visualiser les informations sur les applications flatpak et gérer les flatpaks installés.

## 🚀 Caractéristiques principales:

1. **Visualisation des infos Flatpak:** 📋 peut afficher toutes les informations fournies par la liste flatpak dans une fenêtre graphique conviviale. Chaque élément comporte un bouton pour être facile à copier là où l'on en a besoin..

2. **Gestion des données de l'utilisateur:** 🗑️ Flatpaks stockent des données utilisateur dans un emplacement de système spécifique de votre sytème, souvent laissés-pour-vent lorsqu'une application est désinstallée. Warehouse peut désinstaller une application et supprimer ses données, supprimer des données sans désinstaller, ou simplement vous montrer si une application a des données d'utilisateur.
3. **Actions par lots:** ⚡ Warehouse dispose d'un mode de lot pour des installations rapides, de suppressions de données utilisateur et de copie d'identification d'une application en masse.

4. **Gestion des données de transfert:** 📁 Warehouse scanne le dossier de données de l'utilisateur pour vérifier la présence d'applications installées associées aux données. Si aucune n'est trouvée, il peut supprimer les données ou tenter d'installer un flatpak correspondant.

5. **Gérer les dépôts:** 📦 Les dépôts Flatpak installées et activées peuvent être supprimées, et de nouveaux dépôts peuvent aussi y être ajoutées.

![Various screenshots of Warehouse's abilities](screenshots.png)

## ⏬ Installation:

Warehouse is now available on Flathub! Visit your software store and search for Warehouse, or click this badge.

<a href=https://flathub.org/apps/io.github.flattool.Warehouse><img width='240' alt='Download on Flathub' src='https://dl.flathub.org/assets/badges/flathub-badge-en.png'/></a>

## 🗣️ Traduction
- Translation is hosted with Weblate on Fyra Labs, [click here](https://weblate.fyralabs.com/projects/flattool/warehouse/) to contribute

<a href="https://weblate.fyralabs.com/engage/flattool/">
<img src="https://weblate.fyralabs.com/widget/flattool/warehouse/multi-auto.svg" alt="Translation status" />
</a>

## 💬 Get in Contact
- We have a [Discord Server](https://discord.gg/Sq85C42Xkt) and a [Matrix Space](https://matrix.to/#/#warehouse-development:matrix.org) to discuss and send announcements in!
- You can always open issues, PRs, and use other GitHub features here

## 📜 Code of Conduct
- The Warehouse project follows the [GNOME Code of Conduct](https://wiki.gnome.org/Foundation/CodeOfConduct). See `CODE_OF_CONDUCT.md` for more information.

## ℹ️ Important Notes:
- Warehouse assumes flatpak user data is located in the default directory: `~/.var/app`.
- Warehouse does not aim to replace flatpak; it simply facilitates appropriate flatpak commands for the desired actions.
- This project is still in its early stages, developed by a newcomer. Your understanding of potential bugs is greatly appreciated.

## 🛠️ Installation from Repo Steps:

1. Visit the [releases](https://github.com/flattool/warehouse/releases) page and download `io.github.flattool.Warehouse.flatpak`.
2. Install it using your software store or run the following command:
   ```shell
   flatpak install /path/to/io.github.flattool.Warehouse.flatpak
   ```
You're all set! Launch the application by clicking its icon in your app menu or running:
```shell
flatpak run io.github.flattool.Warehouse
```
