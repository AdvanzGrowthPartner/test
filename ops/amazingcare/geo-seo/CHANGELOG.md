# Changelog · AmazingCare OS GEO/SEO

Cambios aplicados en plataformas (lo más reciente arriba).

| Fecha | Cambio | Por qué | Cómo revertir |
|---|---|---|---|

## 2026-10-20 · Blogs pedidos por Antonia Quezada (OK del usuario el 20-oct)
Todo en Shopify (Blog Amazing). En Notion no se tocó nada.
- **POTS y disautonomía** (`pots-disautonomia-mareos-fatiga-desmayos`, Article/617683517736): oculto, porque Antonia no lo escribió ni lo aprobó. Redirección 301 → `/blogs/noticias/electrolitos-disautonomia` (UrlRedirect/611860381992). *Revertir:* `isPublished:true` y borrar la redirección.
- **Creatina y electrolitos** (`creatina-y-electrolitos-hidratacion`, Article/617683616040): oculto hasta que se relance con texto de Antonia. Redirección 301 → `/blogs/noticias/creatina-beneficios-como-tomarla` (UrlRedirect/611860414760). *Revertir:* igual que el anterior. Al relanzar en la misma URL, borrar antes la redirección.
- **Cyber**: `suplementos-en-cyber-como-comparar` cambia su fecha de publicación del 28-sep al 10-sep 12:00 UTC, y `mejores-electrolitos-chile` del 28-sep al 10-sep 11:00 UTC. Así bajan en el listado y quedan después de Fiestas Patrias. *Revertir:* volver la fecha al 2026-09-28.
- **Alergias** (Article/617683583272): el cuerpo se reemplazó por la versión de Notion corregida por Antonia (sección nueva sobre la relación alergia–sequedad, 3 factores, antihistamínicos de 1ª generación, bibliografía de 3 referencias) y la autora pasa a "Antonia Quezada Zavala". Se mantiene BLOG10. *Revertir:* el cuerpo anterior está en el transcript de la sesión del 19–20 oct; no se guardó copia en el repo.
- **Viajes** (Article/617683550504): cuerpo reemplazado por la versión de Notion de Antonia (humedad de cabina, antes/durante/después del vuelo, bibliografía Zubac + Guéhenneux). **Se quitó "alcohol"** (dos menciones) por la decisión interna del 28-sep. Se mantiene AMAZING10. *Revertir:* igual que Alergias.
- **Nuevo: Electrolitos y quimioterapia** (`electrolitos-quimioterapia-hidratacion`, Article/635071791400): publicado el 20-oct 14:16 UTC, autora Antonia, con title y meta SEO, sin cupón. *Revertir:* `isPublished:false`.
- En los 3 cuerpos (Alergias, Viajes, Quimio) quedaron comentarios HTML invisibles `<!-- FOTO n ... insertar aquí -->` que marcan dónde cargar a mano cada foto.
