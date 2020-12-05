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
    background-video="CurveAnimation.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
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

Remember that the set of points on our curve form a group, so any operation on two of those points must be on the curve.

When adding, we draw a straight line between the two points, find the _third_ point at which they intersect, and then reflect that across the horizontal axis...

---

{{<slide
    background-video="PointAddition.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
>}}

---

Now that we've seen addition, the next step is _multiplication_.

This doesn't mean multiplying two points together, rather, we mean _scalar multiplication_, meaning adding a point to itself multiple times.

---

{{<slide
    background-video="PointDouble.mp4"
    background-position="center"
    background-size="contain"
    style="margin: 1em;"
>}}

---

## Galois Fields

The curves you've seen so are are defined over the plane of real numbers. So there are an infinite number of points that lie on the curve.
