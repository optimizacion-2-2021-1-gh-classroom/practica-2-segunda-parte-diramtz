************
Flujo Máximo
************


El algoritmo de Ford-Fulkerson propone buscar caminos en los que se pueda aumentar el flujo, hasta que se alcance el flujo máximo. Es aplicable a los Flujos maximales. La idea es:

Sea :math:`G(V,E)` un grafo, con :math:`V` vértices, :math:`E` aristas y donde por cada arista :math:`(u,v)`, tenemos una capacidad :math:`c(u,v)` y un flujo :math:`f(u,v)`. Se busca maximizar el valor del flujo desde una fuente :math:`s` hasta un sumidero :math:`t`

El método inicia con :math:`f(u,v)=0` para toda :math:`(u,v) \in  V`. En cada iteración, se incrementa el flujo en :math:`G` mediante el resultado de una búsqueda de un camino de aumento en una red

El flujo a aumentar se debe considerar legal, es decir:

    El flujo de para toda arista :math:`(u,v)` no debe ser mayor que la capacidad de dicha arista. El flujo que sale de la fuente :math:`s` debe ser igual al que llega al sumidero :math:`t`.

Nota: En una red con fuente :math:`s` y sumidero :math:`t` único el valor máximo que puede tomar un flujo variable es igual a la capacidad mínima que puede tomar un corte.

Red residual

Definimos una red residual  :math:`G_{f}(V,E)` como la red donde la capacidad de cada una de las aristas se define como  :math:`c_{f}(u,v) = c(u,v) − f(u,v)` , donde  :math:`c(u,v)` es la capacidad de la arista y el flujo  :math:`f(u,v)` es el flujo de la arista  :math:`(u,v)` en el camino de aumento seleccionado.

Intuitivamente, dado el grafo :math:`G` y un camino de aumento :math:`c_{F}`, la red residual :math:`G_{f}` consiste en el grafo que representa el como cambia la capacidad de cada una de las aristas con respecto al flujo del camino de aumento :math:`c_{F}` en el grafo G.

Caminos de aumento

Un camino de aumento es un camino dirigido de la fuente :math:`s` al sumidero :math:`t` en :math:`G_{f}`, donde la capacidad del camino de aumento es el mínimo de las capacidades de sus aristas.

**Pseudocódigo:**


.. code-block:: bash

    Ford-Fulkerson(G,s,t) {
    Gf = Crear_grafo_residual(G);
    for (cada arista (u,v) de E) {
        f[u,v]= 0;
    }
    while (exista un camino p desde s a t en la red residual Gf) {
        cf(p) = min{cf(u,v): (u,v) está sobre p};
        for (cada arista (u,v) en p) {
            f[u,v]= f[u,v] + cf(p);
            f[v,u]= f[v,u] - cf(p);
        }
        Actualizar_grafo_residual(Gf);
    }

  }





