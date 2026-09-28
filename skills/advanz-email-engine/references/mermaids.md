# Diagramas Mermaid del Email Engine

Estos diagramas van en Notion (uno por página) y en docs. Están validados para el renderer de Mermaid. Copiar el bloque tal cual.

Convención de colores:
- Azul (`#0CB7F2`) = eje / core
- Verde (`#1BB673`) = clave / alto ROI
- Morado (`#7C5CFF`) = loop / data
- Ámbar (`#F5A623`) = optimización
- Gris (`#9DB4BE`) = sistema / al final

---

## GLOBAL · El engine completo (las 8 fases)

```mermaid
flowchart LR
  F1["1 · Captura & Base<br/>¿A quién le hablo?"]
  F2["2 · Bienvenida<br/>¿Qué le ofrezco?"]
  F3["3 · Validación<br/>¿Qué convierte?"]
  F4["4 · Alcance<br/>¿Cómo llego?"]
  F5["5 · Conversión<br/>¿Cómo cierro?"]
  F6["6 · Retención<br/>¿Cómo vuelven?"]
  F7["7 · Feedback<br/>¿Qué dice la gente?"]
  F8["8 · Sistema<br/>¿Qué automatizo?"]

  F1 --> F2 --> F3 --> F4 --> F5 --> F6 --> F7 --> F8
  F8 -. "data vuelve a segmentar" .-> F1
  F7 -. "prueba social" .-> F2
  F7 -. "prueba social" .-> F5

  classDef base fill:#E8F4FB,stroke:#0995C5,color:#08222E;
  classDef core fill:#0CB7F2,stroke:#0995C5,color:#fff;
  classDef sys fill:#EEF1F4,stroke:#9DB4BE,color:#08222E;
  class F1,F3,F4,F7 base;
  class F2,F5,F6 core;
  class F8 sys;
```

---

## GLOBAL · Flywheel (cómo se acelera)

```mermaid
flowchart TD
  W["Mejor Welcome"] --> P["Más 1ª compra"]
  P --> C["Más data de compradores"]
  C --> R["Mejor segmentación"]
  R --> RF["Referidos y recompra"]
  RF --> LTV["Mayor LTV / menor CAC"]
  LTV --> W

  classDef loop fill:#F0EBFF,stroke:#7C5CFF,color:#08222E;
  class W,P,C,R,RF,LTV loop;
```

---

## FASE 1 · Captura & Base

```mermaid
flowchart TD
  V["Visitante anónimo"] --> CAP["Captura de lista<br/>(popup / form + incentivo)"]
  CAP --> DEL["Setup deliverability<br/>SPF · DKIM · DMARC"]
  CAP --> SEG["Segmentación por intención"]
  SEG --> C1["Comprador"]
  SEG --> C2["Carrito"]
  SEG --> C3["Browse"]
  SEG --> C4["Frío"]
  DEL --> INBOX["Llega a la bandeja"]
  CAP --> WEL["→ Welcome (Fase 2)"]

  classDef base fill:#E8F4FB,stroke:#0995C5,color:#08222E;
  classDef data fill:#F0EBFF,stroke:#7C5CFF,color:#08222E;
  class CAP,DEL,INBOX base;
  class SEG,C1,C2,C3,C4 data;
```

---

## FASE 2 · Bienvenida

```mermaid
flowchart LR
  SUB["Se suscribe"] --> E1["Email 1<br/>Bienvenida + cupón<br/>(inmediato)"]
  E1 --> E2["Email 2<br/>Por qué el producto<br/>(+1d)"]
  E2 --> E3["Email 3<br/>Prueba social<br/>(+2d)"]
  E3 --> E4["Email 4<br/>Urgencia cupón<br/>(+4d)"]
  E1 -. "ancla" .-> B["Bundle / producto de entrada"]
  E1 --> X{"¿Compró?"}
  X -- Sí --> OUT["Sale del flujo"]
  X -- No --> E2

  classDef core fill:#0CB7F2,stroke:#0995C5,color:#fff;
  classDef clave fill:#E7F8EF,stroke:#1BB673,color:#08222E;
  class E1,E2,E3,E4 core;
  class B clave;
```

---

## FASE 3 · Validación

```mermaid
flowchart TD
  CAMP["Cada campaña"] --> AB["A/B de asunto y oferta"]
  AB --> VA["Variante A"]
  AB --> VB["Variante B"]
  VA --> WIN["Ganador"]
  VB --> WIN
  WIN -. "se replica" .-> CAMP
  WIN --> REP["→ Reporting (Fase 8)"]
  QZ["Quiz / zero-party data"] --> PERF["Perfil enriquecido"]
  PERF -. "afina" .-> SEG["→ Segmentación (Fase 1)"]

  classDef data fill:#F0EBFF,stroke:#7C5CFF,color:#08222E;
  class AB,VA,VB,WIN,QZ,PERF data;
```

---

## FASE 4 · Alcance

```mermaid
flowchart TD
  BASE["Base segmentada"] --> CAMP["Campañas (calendario)<br/>AON + eventos"]
  CAMP --> SEGV["Versionadas por cohorte"]
  CAMP --> EXCL["Excluye no-activos"]
  VIS["Vio producto, no agregó"] --> BR["Browse Abandonment"]
  BR --> B1["Email 1: ¿lo pensás? (+4h)"]
  B1 --> B2["Email 2: objeción (+1d)"]
  B2 --> B3["Email 3: prueba social (+3d)"]

  classDef vol fill:#FDE9E5,stroke:#E8553B,color:#08222E;
  classDef opt fill:#FDF0DC,stroke:#F5A623,color:#08222E;
  class CAMP,SEGV,EXCL vol;
  class BR,B1,B2,B3 opt;
```

---

## FASE 5 · Conversión

```mermaid
flowchart LR
  ADD["Agrega al carrito"] --> C1["Email 1<br/>Recordatorio sin descuento<br/>(+1h)"]
  C1 --> C2["Email 2<br/>Envío gratis / objeción<br/>(+24h)"]
  C2 --> C3["Email 3<br/>Cupón + urgencia<br/>(+48h)"]
  CHK["Inicia checkout, no paga"] --> K1["Email 1<br/>Recordatorio directo (+30m)"]
  K1 --> K2["Email 2<br/>Urgencia + soporte (+12h)"]
  C1 --> BUY{"¿Compró?"}
  BUY -- Sí --> OUT["Sale"]

  classDef core fill:#0CB7F2,stroke:#0995C5,color:#fff;
  classDef opt fill:#FDF0DC,stroke:#F5A623,color:#08222E;
  class C1,C2,C3 core;
  class CHK,K1,K2 opt;
```

---

## FASE 6 · Retención

```mermaid
flowchart TD
  BUY["Compra"] --> P1["Email 1: gracias + uso (+1d)"]
  P1 --> P2["Email 2: cross-sell (+7d)"]
  P2 --> P3["Email 3: reposición (+28d)"]
  P3 --> P4["Email 4: suscripción (+30d)"]
  BUY --> HAPPY{"¿Cliente feliz?<br/>(review positiva)"}
  HAPPY -- Sí --> REF["Referidos: regala a un amigo"]
  REF --> FRIEND["Amigo recibe -X%"]
  REF --> CREDIT["Referidor gana crédito"]
  CREDIT -. "trae de vuelta" .-> BUY
  P4 --> SUB["Suscripción<br/>ingreso recurrente"]

  classDef clave fill:#E7F8EF,stroke:#1BB673,color:#08222E;
  classDef loop fill:#F0EBFF,stroke:#7C5CFF,color:#08222E;
  class P1,P2,P3,P4 clave;
  class REF,FRIEND,CREDIT,SUB,HAPPY loop;
```

---

## FASE 7 · Feedback

```mermaid
flowchart TD
  DEL["Pedido entregado"] --> REV["Solicitud de review / UGC"]
  REV --> UGC["Reviews + fotos"]
  UGC -. "alimenta" .-> WEL["Welcome (Fase 2)"]
  UGC -. "alimenta" .-> CAR["Carrito (Fase 5)"]
  COLD["No abre 60-90d"] --> WB["Win-back"]
  WB --> W1["Email 1: te extrañamos"]
  W1 --> W2["Email 2: última oportunidad (+5d)"]
  W2 --> SUNSET["Sunset: sale del blast (+10d)"]

  classDef exec fill:#E7F8EF,stroke:#1BB673,color:#08222E;
  classDef opt fill:#FDF0DC,stroke:#F5A623,color:#08222E;
  class REV,UGC exec;
  class WB,W1,W2,SUNSET opt;
```

---

## FASE 8 · Sistema

```mermaid
flowchart LR
  VAL["Flujo con CV% probada<br/>(2-4 semanas de data)"] --> AUTO["Automatizar lo validado"]
  IDEA["Idea no validada"] -. "NO automatizar" .-> STOP["✕ Escala el caos"]
  AUTO --> MON["Monitoreo: no degrada"]
  DATA["Data del mes<br/>flujo + cohorte"] --> REP["Reporting"]
  REP --> LEARN["Qué ganó / qué es peso muerto"]
  LEARN -. "vuelve a" .-> SEG["Segmentación (Fase 1)"]

  classDef sys fill:#EEF1F4,stroke:#9DB4BE,color:#08222E;
  classDef data fill:#F0EBFF,stroke:#7C5CFF,color:#08222E;
  class VAL,AUTO,MON,STOP,IDEA sys;
  class DATA,REP,LEARN data;
```

---

## ESCALAMIENTO · Acciones por facturación

```mermaid
flowchart LR
  R5["5k<br/>4 acciones<br/>6-10 h/mes<br/>1 part-time"]
  R15["15k<br/>9 acciones<br/>20-30 h/mes<br/>1 dedicado"]
  R30["30k<br/>13 acciones<br/>40-55 h/mes<br/>+ producción"]
  R60["60k<br/>16 acciones<br/>70-90 h/mes<br/>+ diseño + análisis"]
  R100["100k<br/>18 acciones<br/>110-140 h/mes<br/>célula"]
  R5 --> R15 --> R30 --> R60 --> R100

  classDef lvl fill:#E8F4FB,stroke:#0995C5,color:#08222E;
  class R5,R15,R30,R60,R100 lvl;
```

---

## DEPENDENCIAS · Email dentro del Growth Engine

```mermaid
flowchart TD
  ACQ["Acquisition<br/>tráfico"] --> EMAIL["EMAIL ENGINE"]
  OFF["Offer<br/>qué vender"] --> EMAIL
  PROD["Producto<br/>que satisfaga"] --> EMAIL
  EMAIL --> CRO["CRO / Tienda<br/>que la PDP convierta"]
  EMAIL --> SYS["Systems / Data<br/>reporting"]
  CONT["Contenido & Diseño<br/>copy + arte"] --> EMAIL
  SYS -. "cierra el loop" .-> EMAIL

  classDef eng fill:#0CB7F2,stroke:#0995C5,color:#fff;
  classDef dep fill:#E8F4FB,stroke:#0995C5,color:#08222E;
  class EMAIL eng;
  class ACQ,OFF,PROD,CRO,SYS,CONT dep;
```
