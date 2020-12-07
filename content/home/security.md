+++
weight = 3
+++

# Security

---

## Diffie-Hellman Key Exchange

Relies on a couple of steps with secret and public values:

 - 2 public values (base and mod)
 - 2 private personal keys
 - 2 public keys
 - 1 private shared key

---

### How does it work?

Lets say Alice and Bob want to exchange information by encrypting it using the D-H key exchange method:

<br><br>

We are going visualize these as colors in a paint can to see how they each use they keys, but take into account these are integers in real life, and they are normally extremely big.


---

{{<slide
    background-video="DHKeyExchange/0001.mp4"
    background-position="center"
    background-size="contain"
    background-transition="none"
    style="margin: 1em;"
    transition="none"
>}}

---

{{<slide
    background-video="DHKeyExchange/0002.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    background-transition="none"
    transition="none"
>}}

---

{{<slide
    background-video="DHKeyExchange/0003.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    background-transition="none"
    transition="none"
>}}

---

{{<slide
    background-video="DHKeyExchange/0004.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    background-transition="none"
    transition="none"
>}}

---

{{<slide
    background-video="DHKeyExchange/0005.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    background-transition="none"
    transition="none"
>}}

---

{{<slide
    background-video="DHKeyExchange/0006.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    background-transition="none"
    transition="none"
>}}

---

{{<slide
    background-video="DHKeyExchange/0007.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    background-transition="none"
    transition="none"
>}}

---

Lets say we have a third person Carlos, that doesn't know any private keys, only the public ones. This means they know the base and mod *g & p*, and both public keys *A & B*. This means that Carlos doesnt know any of *a, b* or *K*. If Carlos were able to get any of these 3 secret keys, then they would be able to calculate *K* the shared private key with which the message are encrypted.

---

These private keys can technically be calculated if *g & p* are not chosen properly. Normally, *p* is a __prime number__ of a __large magnitude__ with *g* being a __coprime__ to *p-1*. The final key is also normally 256 bits long.

These characteristics make it practically impossible for a third person to calculate *K* after its been established, making it extremely safe.
