+++
weight = 20
+++

{{% section %}}

## Elliptic Curves

$$y^2 = x^3 + Ax + B$$

---

### Montgomery and Weierstrass

<br>

The equations we'll be looking at are in _Weierstrass_ form:


$$y^2 = x^3 + Ax + B$$

<br>

There is an alternative form of elliptic curves called _Montgomery_ curves that are of the form:

$$y^2 = x^3 + Ax^2 + x$$

{{% /section %}}

---

{{<slide
    background-video="CurveAnimation/00000.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    transition="none"
>}}

---

{{<slide
    background-video="CurveAnimation/00002.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    transition="none"
>}}

---

{{<slide
    background-video="CurveAnimation/00004.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    transition="none"
>}}

---

{{<slide
    background-video="CurveAnimation/00006.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    transition="none"
>}}

---

### Examples

__Bitcoin__ uses a curve called [secp256k1](https://en.bitcoin.it/wiki/Secp256k1). The equation looks like

$$y^2 = x^3 + 7$$

so $A = 0$ and $B = 7$.

<br>

Many major messaging services including __Whatsapp__ and __Signal__ use a curve called X25519.
The equation of the curve is too big to show here.

---

## Point Addition

Remember that the set of points on our curve form a group, so the result of any operation on two of those points must be a point on the curve.

When adding two points together, we draw a straight line between the two points, find the _third_ point at which they intersect, and then reflect that across the horizontal axis...

---

{{<slide
    background-video="PointAddition/00000.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    transition="none"
>}}

---

{{<slide
    background-video="PointAddition/00001.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    transition="none"
>}}

---

{{<slide
    background-video="PointAddition/00002.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    transition="none"
>}}

---

{{% section %}}

{{<slide
    background-video="PointAddition/00003.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    transition="none"
>}}

---

#### Addition, mathematically

When adding two points, $P = (x_P, y_P)$ and $Q = (x_Q, y_Q)$, we write their sum as $P + Q = R = (x_R, y_R)$.

---

To draw a line between these two points, we calculate the slope between them:

$$\lambda = \frac{y_Q - y_P}{x_Q - x_P}$$

So the equation of the line becomes

$$y = \lambda(x-x_P) + y_P$$

---

We can solve out the equation by plugging this equation back into the curve equation, eventually giving us an equation for the components of the intersection point:

$$x_R = \lambda^2 - x_P - x_Q$$

$$y_R = \lambda(x_P - x_R) - y_P$$

---

This [Desmos graph](https://www.desmos.com/calculator/ialhd71we3) lets you play around with addition of points on an elliptic curve.

{{% /section %}}

---

{{% section %}}

Now that we've seen addition, the next step is _multiplication_.

This doesn't mean multiplying two points together, rather, we mean _scalar multiplication_, meaning adding a point to itself multiple times.

---

{{% /section %}}

---

{{<slide
    background-video="PointDouble/00000.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    transition="none"
>}}

---

{{<slide
    background-video="PointDouble/00001.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    transition="none"
>}}

---

{{% section %}}

{{<slide
    background-video="PointDouble/00002.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
    transition="none"
>}}

---

The method for determining the location of the doubled point is similar to the method of adding, but the main difference is that since we can no longer calculate the "slope" between two points, we instead calculate the derivative at that point:

$$\lambda = \frac{dy}{dx}\Bigr\rvert_{P} = \frac{3x_P^2 + A}{2y_P}$$

The other two formulae are the same.

{{% /section %}}

---

If we wanted to continue do a big point multiplication, like $48798273P$, the method of adding P to itself over and over can get _very_ slow.

Instead, we use a method called __Double and Add__ to quickly calculate the value.

---

Let's say we want to do some computation like $dP$, where $d$ is some integer. We can begin by writing out the _binary expansion_ of $d$. Let's take an easy example, like $d=43$:

$$43 = 2^{5} + 2^{3} + 2^{1} + 2^{0}$$

---

In order to compute $dP = 43p$, we can rewrite our expression as:

$$43P = (2^{5} + 2^{3} + 2^{1} + 2^{0})P = 2^5P + 2^3P + 2^1P + 2^0P$$

So we can begin with $2^0P = P$. We double it to get $2P$, and we add it to $P$. We then double twice more to get $8P$, and add it again, and again with $32P$, and after we add it to our sum, we are left with $43P$.

---

## Discrete Logarithm Problem

<br>
<small>Bringing it back to cryptography.</small>

---

If I gave you some point $X$, which I computed _secretly_ by doing $dP$, and $P$, could you tell me what $d$ is?

This problem is known as the _discrete logarithm problem_, and it is the crux of the secureness of elliptic curve cryptography.

---

The reason __ECC__ is secure is that there are no _known_ methods for efficiently solving $X = dP$ for $d$.

<br>
<small>Just because there are no known methods doesn't mean that one will eventually be discovered. That would be <em>bad</em> news.</small>

---

## Galois Fields

The curves you've seen so are are defined over the plane of real numbers.
So there are an infinite number of points that lie on the curve.

In ECC, we define curves over a [finite field](https://en.wikipedia.org/wiki/Finite_field), or _Galois field_.
The field is most commonly defined over the integers $\mod p$, where $p$ is a prime number. We generally write it as $(\mathbb{Z}_P, +\cdot)$.
