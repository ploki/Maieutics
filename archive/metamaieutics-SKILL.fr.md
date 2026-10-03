---
name: metamaieutics
description: Mener un projet maieutique en autonomie, par procuration. À partir d'un cahier des charges ou d'un projet maieutique existant, Claude rédige un mandat que l'utilisateur valide, puis lance sur une branche git un agent qui applique le skill maieutics pendant que Claude joue le rôle de l'utilisateur. Chaque échange est consigné et commité ; à la fin, un rapport de retour est remis. À utiliser quand l'utilisateur tape /metamaieutics.
---

<!-- Traduction française de SKILL.md, tenue à jour avec lui. SKILL.md fait foi. -->

# Métamaieutique

> Un prompt, puis la délégation. L'utilisateur confie la suite du travail à Claude, qui la mène **en son nom et selon son intention**, sans toucher à sa branche principale.

Réponds dans la langue de l'utilisateur. Ce skill repose sur le skill **maieutics** (`~/.claude/skills/maieutics/SKILL.md`) : relis-le avant de commencer.

## Les rôles

- **L'utilisateur** donne un cahier des charges ou désigne un projet existant, puis **valide le mandat**. C'est sa seule intervention avant le retour.
- **Tu es l'orchestrateur.** Tu rédiges le mandat, crées la branche, lances l'agent, joues le rôle de l'utilisateur par procuration, consignes et commites chaque itération, puis rédiges le rapport de retour.
- **L'agent** applique le skill maieutics dans le dossier. Il ne commite pas, ne change pas de branche, et ne parle qu'à toi.

## 1. Au chargement

1. Explique en deux ou trois phrases ce que fait le skill. Je vais rédiger un mandat, tu le valides, puis je mène le travail seul sur une branche à part. Ta branche principale reste intacte, et c'est toi qui décides à la fin ce que tu gardes.
2. **Identifie le point d'entrée** :
   - **un cahier des charges**, pour un nouveau projet : l'utilisateur décrit le sujet, ce qu'il veut en tirer, et ses contraintes ;
   - **un projet maieutique existant** : un index, un `decision-log.md`, ou un CLAUDE.md qui le déclare. L'utilisateur juge si tu as saisi le sens profond de ce qu'il fait, et son but.
3. **Vérifie git.** Le dossier doit être versionné. S'il ne l'est pas, explique simplement (« git garde une photo de chaque étape et nous permet de travailler sur une copie séparée ») et propose `git init`, suivi d'un premier commit de ce qui est là. S'il y a des modifications non commitées, propose de les commiter d'abord sur la branche courante.

## 2. Le mandat (`mandate.md`)

**Si un `mandate.md` marqué « approuvé » existe déjà** dans le dossier ou sur la branche courante — souvent parce qu'il a été préparé dans une autre session — **ne le réécris pas**. Relis-le avec `author-intent.md`, résume-le en trois lignes pour l'utilisateur, puis passe directement au lancement (section 3), sur la branche existante.

Rédige-le à partir du cahier des charges ou, pour un projet existant, **d'abord à partir de `author-intent.md`**, puis du journal, des décisions de l'auteur lui-même, des sections « Current » et de la mémoire. Si le fichier d'intention n'existe pas, crée-le avant le mandat, puis fais valider les deux ensemble. Il est court et concret :

- **L'intention profonde** : le vrai but (sociétal, personnel, affectif…), les valeurs, ce que l'utilisateur refuse, son ton et ses préférences de travail ;
- **Les objectifs de la branche** et les **critères qui disent qu'ils sont atteints** ;
- **Les livrables attendus**, s'il y en a ;
- **Le nombre maximal d'itérations**, 30 par défaut ;
- **La règle pour les questions hors mandat** : tu la tranches et la marques comme prise par procuration **seulement** si la décision est cohérente avec le mandat et réversible. Si elle est structurante ou irréversible, tu la laisses ouverte et tu la contournes ;
- **Les interdits absolus**, toujours présents :
  - **rien n'est publié** ;
  - **rien n'est envoyé à un service extérieur** : ni mail, ni message, ni dépôt de fichier, ni artifact. La recherche web en lecture seule reste permise, sauf si le mandat l'exclut ;
  - **la branche principale n'est pas touchée** ;
  - **rien n'est retiré de l'historique git**.
- Tout autre interdit que l'utilisateur demande.

**Présente le mandat à l'utilisateur et attends sa validation.** Intègre ses corrections. Rien ne commence sans un oui explicite.

## 3. Le lancement

1. Crée la branche **`metamaieutics/<sujet>-<AAAA-MM-JJ>`** à partir de la branche courante, ou reprends-la si elle existe déjà. Note le nom de la branche de départ ; il servira au retour.
   - **Si une autre session continue de travailler dans le dossier principal**, utilise un **worktree** : `git worktree add ../<dossier>-meta -b <branche>`. La branche est alors extraite dans un dossier séparé et les deux sessions ne se marchent pas dessus. Lance la session métamaieutique dans ce dossier. **Attention** : la mémoire de Claude dépend du chemin du dossier. Recopie la mémoire du projet dans le nouveau dossier, ou rappelle à l'agent de lire le fichier d'intention, l'index, le journal et le glossaire.
   - Pour revenir à la fin, inutile de changer de branche dans le worktree : le rapport explique comment fusionner depuis le dossier principal, puis supprimer le worktree (`git worktree remove`).
2. Commite `mandate.md` sur cette branche et crée `prompt-log.md`.
3. Lance un **agent neuf** (généraliste) avec ces instructions :
   - lis et applique `~/.claude/skills/maieutics/SKILL.md` dans ce dossier. Il ne doit **pas** afficher la bannière ni poser la question du versionnement : l'orchestrateur s'occupe de git ;
   - lis `mandate.md`, `author-intent.md` et, pour un projet existant, l'index, le journal et les notes ;
   - **ne jamais commiter, changer de branche, publier, ni rien envoyer à l'extérieur** ;
   - marque toute décision prise sur ta réponse par procuration comme **par procuration** — `[<id de l'agent> as <id de l'utilisateur>]` — dans les notes et dans le journal, jamais comme venant de l'utilisateur lui-même ;
   - termine chaque tour par trois choses : ce qu'il a fait, quels fichiers ont changé, et les questions ou propositions qu'il soumet à l'utilisateur.

## 4. La boucle

À chaque tour de l'agent :

1. **Lis sa réponse** et regarde ce qui a changé (`git status`, `git diff`).
2. **Réponds comme l'utilisateur, par procuration**, selon le mandat :
   - parle comme l'utilisateur parlerait : son but, ses valeurs, ses préférences, telles que les décrivent le fichier d'intention et le mandat. **Ne modifie pas le fichier d'intention en son nom.** S'il te semble à réviser, dis-le dans le rapport de retour ;
   - **ne sois pas complaisant** : objecte, demande des précisions, refuse ce qui s'écarte du mandat. Le dialogue doit rester une vraie maieutique ;
   - applique la règle des questions hors mandat. Tiens la liste des décisions prises par procuration et des questions laissées ouvertes ;
   - conduis le travail vers les objectifs. Propose la lecture à l'aveugle quand un livrable a été écrit.
3. **Consigne dans `prompt-log.md`** une réécriture propre et concise de ton message, sans rien perdre, avec le numéro d'itération. Le plus récent en tête.
4. **Commite** : `git add -A && git commit -m "metamaieutics: iteration N — <résumé>"`.
5. **Envoie ton message à l'agent** (avec SendMessage) et attends son tour suivant.

Si l'agent perd le fil, par exemple parce que son contexte est saturé, lance-en un neuf : le corpus, le journal et le mandat suffisent à reprendre. C'est la force de la méthode.

## 5. L'arrêt

Arrête-toi dès que l'une de ces conditions est remplie :
- **les objectifs du mandat sont atteints** ;
- **le nombre maximal d'itérations est atteint** ;
- **une question hors mandat bloque la suite.**

## 6. Le rapport de retour (`handback-report.md`)

Rédige-le sur la branche, commite-le, puis **reviens sur la branche de départ**. Il contient :

- **Le résultat** : quels objectifs sont atteints, lesquels ne le sont qu'en partie ou pas du tout, et pourquoi ;
- **Les décisions prises par procuration**, chacune avec sa justification tirée du mandat ;
- **Les hésitations**, c'est-à-dire les endroits où tu n'es pas sûr d'avoir bien représenté l'utilisateur ;
- **Les questions laissées ouvertes**, et la raison de l'arrêt ;
- **Ce qu'il faut relire en premier** ;
- **Comment décider**, expliqué simplement, avec les commandes :
  - pour **voir les différences** : `git diff <branche de départ>..<branche>` ;
  - pour **tout garder** : `git merge <branche>` ;
  - pour **en garder une partie** : ne prendre que certains fichiers ou commits ;
  - pour **jeter la branche** : `git branch -D <branche>`.

Présente ensuite à l'utilisateur un résumé du rapport et le nom de la branche. **C'est lui qui fusionne, en prend une partie, ou la jette** : tu ne fusionnes rien de ton propre chef. Si tu as appris quelque chose de durable sur ses attentes, propose de le consigner en mémoire.
