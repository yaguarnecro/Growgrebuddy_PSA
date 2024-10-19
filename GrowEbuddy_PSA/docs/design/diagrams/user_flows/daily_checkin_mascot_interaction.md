graph TD
    A[Start] --> B[Main Dashboard]
    B --> C[Daily Check-in]
    C --> D[Record Mood]
    D --> E[Mascot Reaction]
    E --> F{Interact with Mascot?}
    F -->|Yes| G[Choose Interaction]
    G --> H[Mascot Response]
    H --> I[Earn Points]
    I --> J[Update Mascot State]
    F -->|No| K[Proceed to Activities]
    J --> K
    K --> L[End]