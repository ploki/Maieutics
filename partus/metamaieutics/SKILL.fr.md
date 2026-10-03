---
name: metamaieutique
description: Mener un projet maieutique en autonomie, par procuration. À partir d'un cahier des charges ou d'un projet maieutique existant, Claude rédige un mandat que l'utilisateur valide, puis il lance sur une branche git un agent qui applique le skill maieutique et joue auprès de lui le rôle de l'utilisateur. Chaque échange est consigné et commité ; à la fin, un rapport de retour est remis. À utiliser quand l'utilisateur tape /metamaieutique.
---

# Métamaieutique

> Un seul prompt, puis la délégation. L'utilisateur confie la suite du travail à Claude, qui la mène **au nom de l'utilisateur et selon son intention**, sans toucher à sa version principale.

Réponds dans la langue de l'utilisateur. Ce skill s'appuie sur le skill **maieutique** (`~/.claude/skills/maieutique/SKILL.md`) : relis-le avant de commencer.

## Rôles

- **L'utilisateur** donne un cahier des charges ou désigne un projet existant, puis **valide le mandat**. C'est sa seule intervention avant le retour.
- **L'orchestrateur, c'est toi.** Tu rédiges le mandat, tu crées la branche, tu lances l'agent, tu joues le rôle de l'utilisateur par procuration, tu consignes et tu commites chaque itération, puis tu rédiges le rapport de retour.
- **L'agent** applique le skill maieutique dans le dossier. Il ne commite pas, ne change pas de branche et ne parle qu'à toi.

## 1. Au chargement

1. Explique en deux ou trois phrases ce que fait le skill. Je vais rédiger un mandat, tu le valides, puis je mène le travail seul sur une branche à part. Ta version principale reste intacte, et tu décideras à la fin ce que tu gardes.
2. **Identifie le point d'entrée** :
   - **un cahier des charges**, pour un nouveau projet : l'utilisateur décrit le sujet, ce qu'il veut obtenir et ses contraintes ;
   - **un projet maieutique existant** : un index, un `journal-des-decisions.md`, ou un CLAUDE.md qui le déclare. L'utilisateur estime que tu as compris le sens profond de sa démarche et son objectif.
3. **Vérifie git.** Le dossier doit être versionné. S'il ne l'est pas, explique simplement (« git garde une photo de chaque étape et permet de travailler sur une copie à part ») et propose `git init`, suivi d'un premier commit de l'existant. S'il y a des modifications non commitées, propose de les commiter d'abord sur la branche courante.

## 2. Le mandat (`mandat.md`)

**S'il existe déjà un `mandat.md` marqué « validé »** dans le dossier ou sur la branche courante, souvent parce qu'il a été préparé dans une autre session, **ne le réécris pas**. Relis-le avec `intention-de-l-auteur.md`, résume-le en trois lignes à l'utilisateur, puis passe directement au lancement (section 3), sur la branche existante.

Rédige-le à partir du cahier des charges ou, pour un projet existant, **d'abord de `intention-de-l-auteur.md`**, puis du journal, des décisions **[G]**, des sections « En vigueur » et de la mémoire. Si le fichier d'intention n'existe pas, crée-le avant le mandat, puis fais-le valider en même temps que le mandat. Il est court et concret :

- **L'intention profonde** : le but réel (sociétal, personnel, affectif…), les valeurs, ce que l'utilisateur refuse, son ton et ses préférences de travail ;
- **Les objectifs de la branche** et les **critères qui permettent de dire qu'ils sont atteints** ;
- **Les livrables attendus**, s'il y en a ;
- **Le nombre maximal d'itérations**, 30 par défaut ;
- **La règle pour les questions hors mandat** : tu tranches et marques **[P]** seulement si la décision est cohérente avec le mandat et réversible. Si elle est structurante ou irréversible, tu la laisses ouverte et tu contournes ;
- **Les interdits absolus**, toujours présents :
  - **rien n'est publié** ;
  - **rien n'est envoyé vers un service extérieur** : ni mail, ni message, ni dépôt de fichier, ni artifact. La recherche web en lecture seule reste permise, sauf si le mandat l'exclut ;
  - **la branche principale n'est pas touchée** ;
  - **rien n'est supprimé de l'historique git**.
- Tout autre interdit que demande l'utilisateur.

**Présente le mandat à l'utilisateur et attends sa validation.** Intègre ses corrections. Rien ne part sans un « oui » explicite.

## 3. Le lancement

1. Crée la branche **`metamaieutique/<sujet>-<AAAA-MM-JJ>`** à partir de la branche courante, ou reprends-la si elle existe déjà. Note le nom de la branche de départ, il servira au retour.
   - **Si une autre session continue de travailler dans le dossier principal**, utilise un **worktree** : `git worktree add ../<dossier>-meta -b <branche>`. La branche est ainsi extraite dans un dossier séparé, et les deux sessions ne se marchent pas dessus. Lance alors la session metamaieutique dans ce dossier. **Attention** : la mémoire de Claude dépend du chemin du dossier. Recopie la mémoire du projet vers celle du nouveau dossier, ou rappelle à l'agent de lire le fichier d'intention, l'index, le journal et le glossaire.
   - Pour revenir à la fin, il n'est pas nécessaire de changer de branche dans le worktree : le rapport indique comment fusionner depuis le dossier principal, puis supprimer le worktree (`git worktree remove`).
2. Commite `mandat.md` sur cette branche et crée `prompt-log.md`.
3. Lance un **agent neuf** (un agent généraliste) avec ces consignes :
   - lire et appliquer `~/.claude/skills/maieutique/SKILL.md` dans ce dossier. Il ne doit **pas** afficher la bannière ni poser la question du versionnement : c'est l'orchestrateur qui gère git ;
   - lire `mandat.md`, `intention-de-l-auteur.md` et, pour un projet existant, l'index, le journal et les notes ;
   - **ne jamais commiter, changer de branche, publier ou envoyer quoi que ce soit vers l'extérieur** ;
   - marquer **[P]** toute décision prise sur ta réponse par procuration, dans les notes comme dans le journal, et non [G] ;
   - terminer chaque tour par trois choses : ce qu'il a fait, les fichiers modifiés, et les questions ou propositions qu'il soumet à l'utilisateur.

## 4. La boucle

À chaque tour de l'agent :

1. **Lis sa réponse** et regarde ce qui a changé (`git status`, `git diff`).
2. **Réponds en tant qu'utilisateur par procuration**, d'après le mandat :
   - parle comme l'utilisateur parlerait : son but, ses valeurs, ses préférences, tels que les décrivent le fichier d'intention et le mandat. **Ne modifie pas le fichier d'intention en son nom.** S'il te semble à revoir, signale-le dans le rapport de retour ;
   - **ne sois pas complaisant** : conteste, demande des précisions, refuse ce qui s'écarte du mandat. Le dialogue doit rester une vraie maïeutique ;
   - applique la règle des questions hors mandat. Garde la liste des décisions **[P]** et des questions laissées ouvertes ;
   - fais avancer le travail vers les objectifs. Suggère la confrontation à l'aveugle quand un livrable est rédigé.
3. **Consigne dans `prompt-log.md`** une réécriture propre et concise de ton message, sans perte d'information, avec le numéro d'itération.
4. **Commite** : `git add -A && git commit -m "metamaieutique: itération N — <résumé>"`.
5. **Envoie ton message à l'agent** (avec SendMessage) et attends son tour suivant.

Si l'agent perd le fil, par exemple parce que son contexte est saturé, relance un agent neuf : le corpus, le journal et le mandat suffisent à reprendre. C'est la force de la méthode.

## 5. L'arrêt

Arrête dès que l'une de ces conditions est remplie :
- **les objectifs du mandat sont atteints** ;
- **le nombre maximal d'itérations est atteint** ;
- **une question hors mandat bloque la suite.**

## 6. Le rapport de retour (`rapport-de-retour.md`)

Rédige-le sur la branche, commite-le, puis **reviens sur la branche de départ**. Il contient :

- **Le résultat** : quels objectifs sont atteints, lesquels ne le sont qu'en partie ou pas du tout, et pourquoi ;
- **Les décisions prises sous procuration [P]**, chacune avec sa justification par le mandat ;
- **Les hésitations**, c'est-à-dire les endroits où tu n'es pas sûr d'avoir bien représenté l'utilisateur ;
- **Les questions laissées ouvertes**, et la raison de l'arrêt ;
- **Ce qu'il faut relire en premier** ;
- **Comment décider**, expliqué simplement, avec les commandes :
  - pour **voir les différences** : `git diff <branche de départ>..<branche>` ;
  - pour **tout garder** : `git merge <branche>` ;
  - pour **garder une partie** : récupérer seulement certains fichiers ou commits ;
  - pour **jeter la branche** : `git branch -D <branche>`.

Présente ensuite à l'utilisateur un résumé du rapport et le nom de la branche. **C'est lui qui fusionne, reprend en partie ou jette la branche** : tu ne fusionnes rien de toi-même. Si tu as appris quelque chose de durable sur ses attentes, propose de l'enregistrer en mémoire.
