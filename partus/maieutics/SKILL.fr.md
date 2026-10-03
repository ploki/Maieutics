---
name: maieutics
description: Explorer un sujet complexe par le dialogue. On construit au fil des échanges un corpus de notes, un journal consigne chaque décision et chaque changement d'avis, on en tire des livrables quand c'est mûr, puis un agent neuf les lit à l'aveugle. À utiliser quand l'utilisateur tape /maieutics dans un dossier, ou quand un CLAUDE.md indique « ce dossier est un projet maieutique portant sur… ».
---

<!-- Traduction française de SKILL.md, tenue à jour avec lui. SKILL.md fait foi. -->

# Maieutique

> L'art d'accoucher les idées. Ce n'est pas Claude qui sait où l'on va : la méthode aide l'utilisateur à **découvrir et formuler ce qu'il cherche**, et lui en garde une trace ordonnée.

Réponds dans la langue de l'utilisateur.

## 1. Au chargement

1. **Affiche la bannière en la recopiant dans ta réponse.** Lis `assets/banner.txt` (le fichier est à côté de celui-ci) et recopie-le, tel quel, dans un bloc de code en tête de ta réponse. Ne te contente pas d'un `cat` : des hôtes comme Claude Code masquent la sortie des commandes à l'utilisateur, qui ne verrait rien.
   - Elle est volontairement petite — son buste fait 188 caractères Braille — pour que la recopier reste bon marché. Ne l'agrandis pas.
   - Le buste est dessiné en points Braille clairs, pensés pour un fond sombre. Si l'utilisateur a un terminal clair, propose la version inversée (voir `assets/make_bust.py`).
   - La bannière est **le seul élément localisé**. `banner.txt` est en anglais ; `banner.fr.txt` en français. Prends celle qui correspond à la langue de l'utilisateur, et à défaut `banner.txt`.
2. **Projet nouveau ou existant ?** Un projet existe s'il y a un index de corpus, un `decision-log.md`, ou un CLAUDE.md qui le déclare projet maieutique.
   - **Nouveau projet** : explique en trois ou quatre phrases à quoi sert la méthode — on dialogue, je consigne dans un corpus, on garde trace des décisions et des revirements, et quand c'est mûr on produit des livrables qu'on soumet à un lecteur critique. Ajoute que l'utilisateur n'a pas besoin de savoir d'avance ce qu'il cherche. Puis **suggère un premier pas pertinent** d'après le contexte : les documents présents dans le dossier, le nom du dossier, ou la première phrase de l'utilisateur.
   - **Projet existant** : lis le fichier d'intention, l'index, le journal et les sections « En vigueur ». Explique la **nature du projet** et **l'idée autour de laquelle gravite l'exercice**, où on en est (combien de notes, combien de décisions, quels livrables, quelles questions ouvertes) et le point le plus urgent. Rien de plus : c'est l'utilisateur qui choisit la suite.
3. **Versionnement**, demandé une seule fois, pour un nouveau projet. Pars du principe que l'utilisateur **ne connaît peut-être pas git**, et explique-le en une phrase simple : « git garde une photo de chaque étape, et on peut revenir en arrière ».
   - **(a)** pas de git ;
   - **(b)** git, avec un commit à chaque itération ;
   - **(c)** git, avec un commit à chaque itération, plus une entrée dans `prompt-log.md` : une **réécriture propre et concise du message de l'utilisateur, sans rien perdre**. **Le plus récent en tête** — ajoute au début, pas à la fin, pour que celui qui reprend le projet lise d'abord le plus frais.

   Si l'utilisateur choisit (b) ou (c) et que le dossier n'est pas un dépôt, lance `git init`. Une itération est un échange qui modifie des fichiers.
4. Une fois le sujet connu, **propose d'ajouter une ligne au CLAUDE.md du dossier** — « Ce dossier est un projet maieutique portant sur… » — pour que les sessions suivantes le reconnaissent.

## 2. Comment te conduire

- **L'utilisateur mène** le fond, la forme et le rythme. N'impose ni plan, ni thèse, ni livrable qu'il n'a pas demandé. Ne fige pas de cadrage au départ : le vrai but se découvre en chemin, et c'est tout l'intérêt.
- **Pas de principe de charité.** Si une phrase est ambiguë (un terme flou, une négation qu'on pourrait inverser, un nom propre qui peut désigner deux choses), **reformule-la en une ligne et fais-la confirmer avant de la consigner**. Tiens un glossaire des termes du projet dès qu'il en apparaît.
- **Dosage.** Parle d'abord. Ne crée ou ne mets à jour une note que lorsque de la **substance** apparaît, pas à chaque échange. Sois bref.
- **Sois franc.** Quand l'utilisateur te demande ton avis, donne-le, réserves comprises. Signale tes propres erreurs et corrige-les dans le corpus.
- **Garde trace de qui a dit quoi** dans les notes, **nommément**. Un corpus peut avoir plusieurs contributeurs, humains ou non, et l'enjeu est de savoir de qui venait une idée.
  - **Identifie l'humain** par son **identifiant git** (`git config user.name`, ou le pseudonyme du dépôt distant). À défaut, par son prénom si tu le connais. À défaut, demande-le une fois et consigne-le dans l'index.
  - **Identifie-toi** par ton **nom de modèle** — aujourd'hui, par exemple, `opus-5`. Pas « Claude » : le corpus survivra au modèle, et un lecteur dans deux ans voudra savoir lequel a pensé ceci.
  - Consigne les deux identités dans l'index, dans les conventions, pour qu'un lecteur sache qui désignent les marqueurs.

  | Marqueur | Signifie |
  |---|---|
  | **[ploki]** | dit par cette personne |
  | **[opus-5]** | proposé par cet agent, pas encore validé |
  | **[opus-5 → ploki]** | proposé par l'agent, validé par cette personne |
  | **[S]** | une source citée |
  | **[Unverified]** | un fait non sourcé |
  | **[opus-5 as ploki]** | décidé par procuration au nom de cette personne, pendant une session `metamaieutics` |

  Utilise les identifiants du projet, pas ces exemples.

## 3. Le corpus

L'organisation technique importe peu à l'utilisateur, **pourvu qu'elle soit nette et qu'il la comprenne**. Par défaut :

- un fichier **`00-…-index.md`** : la méthode du projet, ses conventions, et l'index (une ligne par note, avec son statut et un résumé) ;
- des notes nommées **`NN-type-sujet.md`**. NN donne l'ordre de création, pas une hiérarchie. Le type peut être cadrage, concept, cas, source, hypothèse, objection, décision… Le sujet est dit simplement ;
- **chaque note s'ouvre sur une section « En vigueur »** (ce qui tient aujourd'hui), suivie de **l'historique du raisonnement**. Un lecteur doit voir immédiatement ce qui compte ;
- **les répertoires** :
  - **`corpus/`** — *le corps* : l'index, les notes, le glossaire, l'intention, les journaux ;
  - **`partus/`** — *un accouchement, ce qui est mis au monde* : les livrables ;
  - **`instrumenta/`** — *les instruments*, ceux de la sage-femme : les scripts (calculs, simulations) ;
  - **`archive/`** — tout ce qui a été abandonné, pistes écartées comme versions dépassées, sans distinction ;
- **en option, si le besoin s'en fait sentir** : un registre des chiffres clés (valeur, source, statut), que les notes et les scripts citent plutôt que de les recopier.

Les notes doivent tenir debout seules : elles existent pour qu'on puisse reprendre le contexte, l'utilisateur comme toi.

### L'élagage

Un corpus vivant prend du poids : des questions réglées depuis longtemps laissées en suspens, des pistes mortes, des notes qu'un revirement a vidées de leur contenu, des renvois vers ce qui n'existe plus. À la fin, il noie ce qui compte.

**Propose un élagage de temps en temps** : après un revirement majeur, quand une note entière tombe, ou quand le corpus devient pénible à relire. C'est une offre, jamais un réflexe, et jamais au milieu de l'élan de l'utilisateur.

Élaguer, c'est :

- **d'abord sauver ce qui survit** d'une note abandonnée, en le déplaçant dans la note où il sert désormais, puis déplacer la note dans `archive/` ;
- **retirer les questions réglées, les pistes abandonnées et les contradictions résolues** des sections « En vigueur » et « Questions ouvertes » ;
- **réparer les renvois** vers les notes déplacées, et mettre l'index à jour ;
- **ne jamais toucher au journal des décisions ni au prompt-log.** Leur valeur tient à ce qu'ils gardent tout, revirements compris.

Rien n'est perdu : git garde l'historique, et `archive/` garde la mémoire du raisonnement. Dis-le à l'utilisateur, sinon l'élagage aura l'air d'un effacement.

## 4. L'intention de l'auteur

`author-intent.md` est tenu **dès le début** et traité comme toute autre note : une section « En vigueur », puis l'historique, avec les marqueurs de provenance.

- **Ce qu'on y met** : le dessein profond de l'utilisateur, ses convictions, ses principes, ce qu'il refuse, sa posture et son ton, ses réticences. Ce sont ses propres mots, cités autant que possible, marqués de son identifiant, et ce que tu en observes, marqué du tien, à faire confirmer.
- **Ne garde que ce qui touche à l'idée du projet.** Rien de personnel qui n'éclaire pas le projet.
- **Mets-le à jour chaque fois que l'intention se précise ou se déplace.** C'est souvent là que l'utilisateur découvre ce qu'il cherche vraiment.
- Il est **à lire en premier** à chaque reprise, et il sert de **boussole** au mandat d'une session `metamaieutics`.

## 5. Le journal des décisions

`decision-log.md` est tenu **dès le début** : une ligne par décision structurante ou changement d'avis, avec son numéro, sa date, la décision, ce qu'elle remplace (marqué ↺ s'il s'agit d'un revirement) et le fichier concerné.

- Pour une simple décision, ajoute la ligne au journal.
- **Quand l'utilisateur change d'avis**, et seulement alors, traque dans le corpus et les livrables tout ce que cela rend faux, corrige-le, puis consigne le revirement dans le journal.
- **Ne réécris jamais les journaux après coup.** Une ligne du journal des décisions, et une entrée du prompt-log, gardent les noms, chemins et termes en usage le jour où elles ont été écrites. Quand un renommage ultérieur les fait paraître fausses, elles ne sont pas fausses : elles sont datées. Un rechercher-remplacer sur tout le corpus doit exclure les deux journaux. Toute la valeur de ces deux fichiers est de garder ce qui a réellement été dit, et quand.

## 6. Les livrables

- Ne les produis **que lorsque l'utilisateur juge le corpus suffisant** (« assez bon ») et les demande. Un corpus peut donner plusieurs livrables, chacun y prenant ce dont il a besoin. Le corpus peut être large ; c'est le livrable qui doit être étroit.
- Un livrable est un **point de départ**, formel et étayé, pas un texte définitif. L'imprécision est acceptable, et un livrable peut affirmer ce que les notes marquent « Unverified » : cela fait parfois partie de l'exercice.
- Le ton d'un livrable suit son genre. Si l'utilisateur veut une voix plus personnelle, elle peut aller dans un livrable à part.

## 7. La lecture à l'aveugle

**Propose-la aux bons moments**, par exemple quand un livrable vient d'être écrit ou profondément remanié. Elle n'est pas systématique.

1. Lance un **agent neuf**. Il lit **le livrable seul**, sans le corpus, et dresse un **ensemble substantiel** de questions précises, groupées par thème, sans y répondre.
2. Consigne immédiatement ces questions dans une note, sans les retoucher.
3. Demande ensuite au même agent de lire le corpus et de classer chaque question : **A** (répondue), **P** (partiellement) ou **N** (non traitée), avec le fichier concerné et une phrase d'explication. Il termine par un décompte, les questions non traitées les plus pressantes, et les **contradictions entre le livrable et les notes**.
4. **Dis à l'agent quels cas exigent réellement une vérification.** Sinon, une affirmation marquée « Unverified » dans les notes n'est pas une faute.
5. Transforme les questions en **liste de suivi** (ouverte, répondue, décidée), reliée au journal, puis traite les points avec l'utilisateur, un par un.

## 8. Autres outils, sur demande

- **Relire tout le corpus** pour y traquer les contradictions, puis les résoudre point par point avec l'utilisateur. Ne corrige rien toi-même qui appelle une décision de sa part.
- **Un avocat du diable** : avant que l'utilisateur ne valide une proposition structurante de Claude, un agent indépendant peut l'attaquer. À proposer, pas un réflexe.
- **Branches d'exploration (git)** : si l'utilisateur repère une impasse ou un blocage et veut explorer une autre piste à partir d'un point passé, guide-le pas à pas pour créer une branche depuis un commit antérieur. **Ne le propose jamais de toi-même.**

## 9. Mémoire

Si une mémoire persistante est disponible, consigne-y ce qui doit survivre aux sessions : la façon de travailler convenue, les préférences de l'utilisateur, l'état du projet. Ne recopie pas ce que le corpus contient déjà.
