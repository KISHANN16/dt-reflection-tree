# Daily Reflection Tree

This project implements a deterministic reflection tool using a decision tree.

## How it works

* The user answers fixed-choice questions
* The tree branches deterministically
* Signals track user tendencies across 3 axes:

  * Axis 1: Agency (internal vs external)
  * Axis 2: Contribution vs entitlement
  * Axis 3: Radius of impact

## Files

* reflection-tree.tsv → main tree structure
* write-up.md → design explanation

## Notes

* No LLM is used at runtime
* Fully deterministic structure
