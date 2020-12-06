## Modular Arithmetic

If we say we have a set of *integers module p* called $Z_p$.  
This means that $Z_p = {0, 1, ..., p-1} = [0, p-1]$.  
If a calculation were to land outside of this range, it would wrap back around to the start in modulo calculations.

---

### Example

Lets say we were working with *mod 7*. Here are a couple of calculations that could happen:   
$1 + 1 = 2, 2 + 1 = 3, 3 + 1 = 4, 4 + 1 = 5, 5 + 1 = 6, 6 + 1 = 0$
This last one is zero because, its larger than *p - 1* meaning that it wraps back to the start.

---

### Congruence

We can also say that two integers are __congruent modulo p__, written $a \equiv b (mod p)$, if and only if there exists a *k* such that $a - b = kp$.  
This means that we can convert between *a* and *b* by adding or subtracting *p* repeatedly. This also means that we can bring both *a* and *b* into the range of $Z_p$ by adding or subtracting multiples of *p*, which we call __reduction modulo p__

---

### Why is Modular Arithmetic Useful/Important

One reason why Modular Arithmetic is used so often in computing is that it allows us to represent values in a set number of bits, even if the number we are representing wouldn't fit. This is because we decrease the number to fit in *mod p*, and if we set *p* to a set number of bits, any *mod p* calculation will be less than that number of bits.

---

## Group Theory

---

### Abelian Groups

An *abelian group* is a set $E$ together with a an operation $\bullet$. This operation combines to elements of a set, called *a, b*, such that $a, b \in E$. It also has 5 other requirements listed in the next slide:

---

### $\bullet$ Requirements

__Closure:__ If $a, b \in E$ then $a \bullet b \in E$.

__Commutativity:__ For all $a, b \in E$, $a \bullet b = b \bullet a$.  

__Associativity:__ For all $a, b, c \in E$, we have $(a \bullet b) \bullet c = a \bullet (b \bullet c)$.   

__Identity Element:__ There exists an element *i* in *E* such that $a \in E$, $a \bullet i = a$. This is called the *identity* or *nautral* element.

__Inverse Element:__ For every $a \in E$ there exists an element $b$ such that $a \bullet b = i$, where $i$ is the *identity element*. This also means that we call *b* the *inverse* of *a*, also written $b = a^{-1}$.

---

### Other Characteristics of Abelian Groups
- The number of elements in *E* is called the *order* of the group.  
- Two groups with the same *prime order* are *__isomorphic__ from each other, meaning one group can be transformed to the other by renaming/reordering the elements.

---
## Diffie-Hellman Key Exchange

Relies on a couple of steps with secret and public values:

 - 2 public values (base and mod)
 - 2 private personal keys
 - 2 public keys
 - 1 private shared key

---


### How does it work?

Lets say Alice and Bob want to exchange information by encrypting it using the D-H key exchange method:   <br> <br>
We are going visualize these as colors in a paint can to see how they each use they keys, but take into account these are integers in real life, and they are normally extremely big.

---

{{<slide
    background-video="DHKeyExchange.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
>}}

---

Lets say we have a third person Carlos, that doesn't know any private keys, only the public ones. This means they know the base and mod *g & p*, and both public keys *A & B*. This means that Carlos doesnt know any of *a, b* or *K*. If Carlos were able to get any of these 3 secret keys, then they would be able to calculate *K* the shared private key with which the message are encrypted.

---

These private keys can technically be calculated if *g & p* are not chosen properly. Normally, *p* is a __prime number__ of a __large magnitude__ with *g* being a __coprime__ to *p-1*. The final key is also normally 256 bits long.

These characteristics make it practically impossible for a third person to calculate *K* after its been established, making it extremely safe.
