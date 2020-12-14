+++
weight = 1
+++

# Modular Arithmetic

---

{{% section %}}

If we say we have a set of *integers modulo p* called $\mathbb{Z}_p$, this means that $\mathbb{Z}_p = \\{0, 1, ..., p-1\\}$.
If a computation on any two elements in this set were to land outside of this range under normal circumstances, it would instead wrap back around to the other end.

<br>
<small>Let's see an example</small>

🔽

---

### Example

Let's say we are working in $\text{mod } 7$.
Then we have the following:

$$1 + 1 \equiv 2$$
$$2 + 1 \equiv 3$$
$$3 + 1 \equiv 4$$
$$4 + 1 \equiv 5$$
$$5 + 1 \equiv 6$$
$$6 + 1 \equiv 0$$

This last sum is zero because it is larger than $p - 1$, so it wraps around to the beginning.

{{% /section %}}

---
{{% section %}}

### Congruence

We can also say that two integers are _congruent modulo p_, written $a \equiv b \pmod p$, if and only if there exists a $k$ such that $a - b = kp$.

This means that we can convert between $a$ and $b$ by adding or subtracting $p$ repeatedly.
This also means that we can bring both $a$ and $b$ into the range of $\mathbb{Z}_p$ by adding or subtracting multiples of $p$, which we call _reduction modulo p_.    
<br>
<small>Let's see an example</small>

🔽

---

### Example

Let's say we are working in $\text{mod } 7$.
Then we have the following:

9 - 2 = k(7)
7 = 7

9 mod 7 = 2 mod 7

We can see that 9 seems to be out of the range of $\mathbb{Z}_p$, but by using $mod p$ we make sure its still in range.


---

### Why is Modular Arithmetic Useful/Important

One reason why modular arithmetic is used so often in computing is that it allows us to represent values in a finite number of bits, even if the number we are representing wouldn't fit.
This is because we decrease the number to fit in $\text{mod } p$, and if we set $p$ to a set number of bits, any $\text{mod }p$ calculation will be less than that number of bits.
