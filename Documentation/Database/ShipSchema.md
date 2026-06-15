# Ship Schema

**Project:** The Poneglyph – Road to the OPTC

**Version:** 1.0

**Status:** Approved

---

# Purpose

The Ship Schema defines every piece of information that can be stored for a ship.

Every ship in The Poneglyph must follow this schema.

This document serves as the single source of truth for ship data.

---

# Design Principles

* Every ship has one permanent ID.
* Every field has one purpose.
* No duplicated information.
* No calculated values are stored.
* Missing data is preferred over guessed data.
* Every recommendation must be explainable.

---

# Naming Convention

Every ship receives a permanent identifier.

Examples

```text
ship.dinghy

ship.thousand_sunny

ship.shark_superb

ship.oro_jackson

ship.zunesha
```

The Ship ID never changes.

Display names may change if Bandai changes localization.

---

# Required Fields

| Field             | Type    | Description                   |
| ----------------- | ------- | ----------------------------- |
| ShipID            | String  | Permanent internal identifier |
| DisplayName       | String  | Official in-game ship name    |
| ReleaseVersion    | String  | Game version when released    |
| AcquisitionMethod | Enum    | How the ship is obtained      |
| MaxHP             | Integer | Maximum HP                    |
| MaxATK            | Integer | Maximum ATK                   |
| MaxRCV            | Integer | Maximum RCV                   |

---

# Ship Abilities

## Base Ability

Exact Lv10 ship ability.

Stored exactly as written in-game.

---

## Lv11 Ability

Exact Lv11 upgrade.

---

## Lv12 Ability

Exact Lv12 upgrade.

---

## Ship Special

Exact ship special.

---

## Ship Modification 1

First modification unlocked at Lv12.

---

## Ship Modification 2

Second modification unlocked at Lv12.

---

# Restrictions

| Field                | Description                      |
| -------------------- | -------------------------------- |
| Required Classes     | Classes benefiting from the ship |
| Required Types       | Types benefiting from the ship   |
| Captain Restrictions | Captain requirements             |
| Crew Restrictions    | Crew requirements                |

---

# Gameplay Ratings

Every ship receives ratings from 1–5.

| Rating            | Description            |
| ----------------- | ---------------------- |
| Damage            | Offensive potential    |
| Utility           | General usefulness     |
| Survivability     | Defensive value        |
| Farming           | Farming efficiency     |
| Flexibility       | Number of viable teams |
| Beginner Friendly | Easy to use            |
| Endgame Value     | High-level usefulness  |

Ratings must always be supported by documented reasoning.

---

# Tags

Ships are categorized using standardized tags.

Examples

## Content

* content.kizuna
* content.treasure_map
* content.pirate_king_adventures
* content.grand_voyage
* content.arena
* content.grand_party

## Classes

* class.free_spirit
* class.slasher
* class.powerhouse
* class.cerebral
* class.driven
* class.shooter
* class.fighter
* class.striker

## Types

* type.str
* type.dex
* type.qck
* type.psy
* type.int

## Roles

* role.damage
* role.cooldown
* role.utility
* role.experience
* role.survivability
* role.universal

---

# Recommendation Fields

Every recommendation must include a reason.

| Field                | Description                    |
| -------------------- | ------------------------------ |
| RecommendedCaptains  | Captains that synergize well   |
| RecommendedContent   | Best game modes                |
| Strengths            | Main advantages                |
| Weaknesses           | Main disadvantages             |
| UpgradePriority      | Should players invest?         |
| RecommendationReason | Why this recommendation exists |

---

# Verification

Every ship entry has a verification status.

| Status       | Meaning               |
| ------------ | --------------------- |
| Verified     | Confirmed in-game     |
| Needs Review | Awaiting verification |
| Incomplete   | Missing information   |
| Deprecated   | No longer current     |

---

# Future Expansion

The schema is designed to support future additions without breaking compatibility.

Possible future fields include:

* Ship Image
* Ship Icon
* Release Date
* Patch History
* Related Ships
* Community Rating
* Last Updated
* Data Source
* Notes

---

# Golden Rule

Every piece of ship information should exist exactly once.

All interfaces—including Excel, future web tools, and any companion applications—must read from the same underlying data.

The schema is the foundation upon which every ship-related feature of The Poneglyph is built.

