+++
weight = 2
+++

# Group Theory

---

## Abelian Groups

An *abelian group* is defined by a set $E$ together with a an operation $\bullet$.
This operation combines two elements $a,b \in E$.
Abelian groups follow five other axioms...

---

### Axioms

{{% fragment %}}
__Closure:__ If $a, b \in E$ then $a \bullet b \in E$.
{{% /fragment %}}

{{% fragment %}}
__Commutativity:__ For all $a, b \in E$, $a \bullet b = b \bullet a$.
{{% /fragment %}}

{{% fragment %}}
__Associativity:__ For all $a, b, c \in E$, $(a \bullet b) \bullet c = a \bullet (b \bullet c)$.
{{% /fragment %}}

{{% fragment %}}
__Identity Element:__ There exists an element $I$ in $E$ such that $a \in E$, $a \bullet I = a$. This is called the *identity* or *nautral* element.
{{% /fragment %}}

{{% fragment %}}
__Inverse Element:__ For every $a \in E$ there exists an element $b$ such that $a \bullet b = I$, where $I$ is the *identity element*. This also means that we call $b$ the *inverse* of $a$, also written $b = a^{-1}$.
{{% /fragment %}}

---

### Other Characteristics of Abelian Groups

- The number of elements in *E* is called the *order* of the group.
- If two groups have the same order, and that order is a *prime* number (called *prime order groups*), the groups are _isomorphic_ to one another.
  - This means one group can be "transformed" into another group by renaming or reordering the elements
