+++
weight = 20
+++

## Elliptic Curves

{{% fragment %}} $$y^2 = x^3 + Ax + B$$ {{% /fragment %}}

---

{{<slide
    background-video="CurveAnimation.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
>}}

---

There are two parameters that define elliptic curves:

<br>

$A$ &nbsp; and &nbsp; $B$

---

### Examples

__Bitcoin__ uses a curve called [secp256k1](https://en.bitcoin.it/wiki/Secp256k1). The equation looks like

$$y^2 = x^3 + 7$$

so $A = 0$ and $B = 7$.

<br>

Many major messaging services including __Whatsapp__ and __Signal__ use a curve called X25519.
The equation of the curve is too big to show here.

---

### Montgomery and Weierstrass

The equations we've been looking at are in _Weierstrass_  form, that is: $y^2 = x^3 + Ax + B$.

There is an alternative form of elliptic curves called _Montgomery_ curves that are of the form: $y^2 = x^3 + Ax^2 + x$.

<br>
<small>But we'll be focusing on Weierstrass curves today.</small>

---

## Galois Fields and Elliptic Curves

