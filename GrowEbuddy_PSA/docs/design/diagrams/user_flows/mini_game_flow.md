graph TD
    A[Start] --> B[Main Dashboard]
    B --> C[Mini-Games Section]
    C --> D{Choose Game}
    D -->|Memory Pairs| E[Start Memory Pairs]
    D -->|Simon Says Breath| F[Start Simon Says Breath]
    E --> G[Play Game]
    F --> G
    G --> H{Complete Game?}
    H -->|Yes| I[Show Results]
    H -->|No| J[Option to Retry]
    I --> K[Award Points/Achievements]
    J --> G
    K --> L[Update Progress]
    L --> M[Return to Dashboard]
    M --> N[End]