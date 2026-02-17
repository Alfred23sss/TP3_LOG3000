# LOG3000 - TP3

## Page de couverture

- Cours: LOG3000
- Travail: TP3 - Gestion de versions, documentation, tests et correction de bogues
- Equipe: [REPLACE_WITH_YOUR_TEAM_NUMBER]
- Depot GitHub: `https://github.com/Alfred23sss/TP3_LOG3000`
- Date: 2026-02-17

---

## 1) Mise en place du depot (etat)

Cette phase etait deja completee au debut du travail:
- Depot GitHub initialise.
- Collaborateurs deja ajoutes.
- Base de code deja poussee.

Un README initial a ensuite ete enrichi pour inclure les informations requises (objectif, prerequis, installation, usage, tests, contribution).

## 2) Documentation du code et des modules

Le projet a ete documente a trois niveaux:

1. **Documentation Python (backend)**
   - Ajout de docstrings dans `app.py` et `operators.py`.
   - Ajout de commentaires concis pour clarifier les choix de validation d'expressions.

2. **Documentation de modules**
   - `TP3---LOG3000-main/README.md`
   - `TP3---LOG3000-main/templates/README.md`
   - `TP3---LOG3000-main/static/README.md`
   - `TP3---LOG3000-main/tests/README.md`

3. **README principal**
   - Description complete du projet.
   - Etapes d'installation.
   - Instructions d'utilisation.
   - Procedure d'execution des tests.
   - Flux de contribution (issues, branches, PR).

## 3) Ajout de tests et detection de bogues

Une suite `pytest` a ete ajoutee:
- `tests/test_operators.py`
- `tests/test_app.py`

Les tests ont permis d'identifier 4 bogues reels:
1. Soustraction calculee a l'envers.
2. Multiplication implementee avec l'operateur de puissance.
3. Division entiere au lieu de division reelle.
4. Libelles UI incorrects/manquants dans le template HTML.

Resultat initial observe: **4 echecs, 6 succes**.

## 4) Suivi des problemes (Issues GitHub)

Pour chaque bogue confirme, une issue dediee a ete creee:
- Issue #1: UI labels incorrects/manquants
- Issue #2: Soustraction inversee
- Issue #3: Multiplication incorrecte
- Issue #4: Division avec perte de precision

Chaque issue contient:
- description du probleme,
- comportement attendu vs reel,
- reproduction via test echoue.

## 5) Corrections par branches dediees

Une branche par issue a ete utilisee:
- `fix/issue-1-ui-labels`
- `fix/issue-2-subtract`
- `fix/issue-3-multiply`
- `fix/issue-4-divide`

Corrections appliquees:
- `subtract`: `a - b`
- `multiply`: `a * b`
- `divide`: `a / b`
- `index.html`: correction des libelles (`2`, `8`, `*`, `/`)

Chaque branche contient:
- un correctif cible,
- rerun du test associe,
- commit avec message explicite.

## 6) Pull Requests, revue et fusion

Une PR par branche a ete ouverte puis fusionnee:
- PR #5 (issue #1)
- PR #6 (issue #2)
- PR #7 (issue #3)
- PR #8 (issue #4)

Les PR referencent les issues et documentent le plan de test.
La fusion sur `main` a ete effectuee apres verification.

## 7) Validation finale

Suite complete executee sur `main`:
- **10 tests passes, 0 echec**

Ce resultat confirme:
- correction des 4 bogues identifies,
- absence de regression sur les autres cas testes,
- coherence globale frontend/backend.

## 8) Checklist finale de remise

- [x] Depot GitHub disponible.
- [x] Documentation completee (README principal + readme de modules + docstrings).
- [x] Tests ajoutes et documentes.
- [x] Issues creees et fermees.
- [x] Branches de correction dediees.
- [x] PR creees et fusionnees.
- [x] Tests finaux 100% passants.
- [ ] Equipe a renseigner dans le README et rapport (`[REPLACE_WITH_YOUR_TEAM_NUMBER]`).
- [ ] S'assurer que le depot est public a la date limite.
