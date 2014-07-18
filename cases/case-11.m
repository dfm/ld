(* Define the geometric model *)
k1 := ArcCos[(1 - p^2 + z^2) / (2*z)];
k0 := ArcCos[(p^2 + z^2 - 1) / (2*p*z)];
Fe := 1 - Piecewise[{
    {0, 1+p/r<z/r},
    {((p/r)^2 * k0 + k1 - Sqrt[(z/r)^2 - ((1+(z/r)^2-(p/r)^2)^2)/4])/Pi,
           Abs[1-(p/r)] < (z/r) && (z/r) <= 1+(p/r)},
    {(p/r)^2, (z/r) <= 1-(p/r)},
    {1, (z/r) <= (p/r) - 1}
}];

(* Define the intensity model *)
mu := Sqrt[1-r^2];
Ir := 1 - g1 * (1-mu) - g2 * (1-mu)^2;

(* Pre-compute/simplify some quantities *)
Dr := D[Fe * r^2, r];
norm := Integrate[2*r*Ir, {r, 0, 1}];
ass := Simplify[g1 + g2 < 1 && z >= 0 && p > 0 && !(z == 0 && p < 1) && !(z <= p - 1) && !(z < p && z < 1-p) && !(z < p && z == 1-p) && !(z < p) && !(z == p && z < 1 - p) && !(z == 1/2 && p == 1/2) && !(z == p) && !(z < 1 - p) && !(z == 1 - p) && (z < 1 + p)];
integrand := Simplify[Ir * Dr, Assumptions -> ass];

(* Do the real integral *)
Print[Integrate[integrand, {r, 0, 1}, Assumptions -> ass] / norm]
