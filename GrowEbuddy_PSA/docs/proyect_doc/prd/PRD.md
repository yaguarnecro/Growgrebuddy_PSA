# Product Requirements Document (PRD) for GrowEbuddy P.S.A.

## Table of Contents
- [Product Requirements Document (PRD) for GrowEbuddy P.S.A.](#product-requirements-document-prd-for-growebuddy-psa)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
  - [2. Game Concept](#2-game-concept)
  - [3. Objectives](#3-objectives)
  - [4. Target Audience](#4-target-audience)
    - [Primary Audience: **Young Adults (18-35)**](#primary-audience-young-adults-18-35)
    - [Secondary Audience: **Transgenerational Users**](#secondary-audience-transgenerational-users)
    - [Personas](#personas)
  - [5. User Stories](#5-user-stories)
  - [6. Use Cases](#6-use-cases)
  - [7. Product Overview](#7-product-overview)
  - [8. Key Features and Functional Requirements](#8-key-features-and-functional-requirements)
    - [8.1 Virtual Mascot ⭐](#81-virtual-mascot-)
    - [8.2 Virtual Spaces ⭐](#82-virtual-spaces-)
    - [8.3 Point System](#83-point-system)
    - [8.4 Mini-Games](#84-mini-games)
    - [8.5 User Progression ⭐](#85-user-progression-)
    - [8.6 Game Mechanics](#86-game-mechanics)
    - [8.7 User Onboarding Process](#87-user-onboarding-process)
    - [8.8 Social Features](#88-social-features)
    - [8.9 Accessibility Features](#89-accessibility-features)
    - [8.10 Data and Privacy](#810-data-and-privacy)
  - [9. Technical Requirements](#9-technical-requirements)
    - [9.1 Platform](#91-platform)
    - [9.2 Frontend](#92-frontend)
    - [9.3 Backend](#93-backend)
    - [9.4 Database](#94-database)
    - [9.5 Deployment](#95-deployment)
    - [9.6 Additional Technologies](#96-additional-technologies)
  - [10. Monetization](#10-monetization)
  - [11. Success Metrics](#11-success-metrics)
  - [12. Timeline](#12-timeline)
  - [13. Risks and Mitigation Strategies](#13-risks-and-mitigation-strategies)
  - [14. Market Analysis](#14-market-analysis)
    - [14.1 Competitors](#141-competitors)
    - [14.2 **Unique Selling Points** (**USPs**)](#142-unique-selling-points-usps)
    - [14.3 Market Positioning](#143-market-positioning)
    - [14.4 Market Trends](#144-market-trends)
    - [14.5 Growth Opportunities](#145-growth-opportunities)
  - [15. Design Guidelines](#15-design-guidelines)
    - [15.1 Visual Style Guide](#151-visual-style-guide)
      - [**Color Palette**](#color-palette)
      - [Typography](#typography)
      - [Iconography](#iconography)
    - [15.2 UI Components](#152-ui-components)
    - [15.3 Layout Guidelines](#153-layout-guidelines)
    - [15.4 User Experience Principles](#154-user-experience-principles)
    - [15.5 Accessibility Guidelines](#155-accessibility-guidelines)
    - [15.6 Localization Considerations](#156-localization-considerations)
    - [15.7 Mascot Design Guidelines](#157-mascot-design-guidelines)
    - [15.8 Gamification Elements](#158-gamification-elements)
    - [15.9 Onboarding Design](#159-onboarding-design)
    - [15.10 Responsive Design Principles](#1510-responsive-design-principles)
  - [16. Future Enhancements](#16-future-enhancements)
    - [16.1 Additional Virtual Spaces](#161-additional-virtual-spaces)
    - [16.2 Expanded Point System](#162-expanded-point-system)
    - [16.3 More Mini-Games](#163-more-mini-games)
    - [16.4 Advanced Technical Features](#164-advanced-technical-features)
    - [16.5 Enhanced Monetization](#165-enhanced-monetization)
    - [16.6 Advanced Analytics and Reporting](#166-advanced-analytics-and-reporting)

## 1. Introduction

**GrowEBuddy P.S.A.** is a gamified personal development application that combines elements of virtual pet care, habit tracking, and mental wellness to help users improve their overall well-being. 
*The initials **"P.S.A."** stand for both **"Personal Support Assistant"** and **"Play, System, App,"**  reflecting the project's multifaceted approach to personal growth and development*.

## 2. Game Concept

GrowEBuddy P.S.A. is a mobile app that gamifies personal growth and development. Users nurture a virtual mascot that represents their inner self, evolving and growing as they engage in various activities and challenges. The app combines elements of:

- **Virtual pet care**: Users care for their mascot, which responds to their actions and progress.
- **Habit tracking**: Daily tasks and challenges encourage users to form positive habits.
- **Mental wellness**: Meditation, reflection, and mindfulness exercises promote mental health.
- **Personal development**: Skill-building activities and challenges foster personal growth.

*The app is designed to be engaging, visually appealing, and easy to use, with a colorful, minimalist interface that appeals to young adults while remaining accessible to users of all ages*.

## 3. Objectives

The **primary objectives** of GrowEbuddy P.S.A. are:

1. To encourage users to engage in daily personal development activities.
2. To promote mental wellness through guided exercises and reflection.
3. To foster habit formation through gamification and rewards.
4. To provide a sense of progress and achievement in personal growth.
5. To create a supportive community of users working towards self-improvement.

## 4. Target Audience

### Primary Audience: **Young Adults (18-35)**
- Tech-savvy individuals comfortable with mobile apps
- People interested in personal development and self-improvement
- Users who enjoy gamification and virtual pet experiences

### Secondary Audience: **Transgenerational Users**
- Adults of any age interested in personal growth
- Parents looking for a family-friendly app to teach children about self-care and responsibility
- Educators or counselors seeking tools to support their clients' personal development

### Personas

1. **Alex, 25 - Young Professional**
   - Busy schedule, looking for ways to incorporate self-care into daily routine
   - Enjoys mobile games but wants something more meaningful
   - Interested in meditation and mindfulness but struggles to maintain a consistent practice

2. **Sam, 32 - Parent and Freelancer**
   - Balancing work and family life, needs flexible personal development tools
   - Wants to model good habits for their children
   - Enjoys the idea of "growing" something over time

3. **Jordan, 19 - College Student**
   - Dealing with stress from studies and social life
   - Looking for fun ways to develop life skills and emotional intelligence
   - Enjoys social aspects of apps and sharing achievements with friends

## 5. User Stories

1. As a busy young professional, I want to easily track my daily habits and mood, so that I can see my progress over time and stay motivated.

2. As a meditation beginner, I want guided mindfulness exercises, so that I can learn to manage stress and improve my focus.

3. As a parent, I want to use the app with my children, so that we can learn about personal growth and responsibility together.

4. As a college student, I want to challenge myself with skill-building activities, so that I can develop practical life skills while having fun.

5. As a user interested in self-reflection, I want prompts and exercises that encourage introspection, so that I can gain deeper insights into myself.

## 6. Use Cases

1. **Daily Check-in and Mascot Care**
   - User opens the app
   - User records their mood and energy levels
   - User completes daily tasks to care for their mascot (e.g., feeding, playing)
   - User receives rewards and sees their mascot respond positively

2. **Completing a Mindfulness Exercise**
   - User enters "The Cave" virtual space
   - User selects a guided meditation exercise
   - User follows the meditation instructions
   - User completes the exercise and earns points
   - User's mascot gains "Awareness" attribute points

3. **Participating in a Skill-building Challenge**
   - User enters the "Samsara" virtual space
   - User chooses a weekly skill-building challenge
   - User completes daily tasks related to the challenge
   - User logs their progress and reflections
   - User earns rewards and sees their mascot evolve

4. **Engaging with the Community**
   - User visits the community section
   - User shares a recent achievement or reflection
   - User views and interacts with posts from other users
   - User participates in a community challenge
   - User earns social engagement points

5. **Customizing the Virtual Space**
   - User earns enough in-game currency
   - User visits the customization shop
   - User selects new items or themes for their virtual spaces
   - User applies the customizations
   - User's mascot reacts positively to the changes

## 7. Product Overview

The app features a virtual mascot that evolves based on user interactions and progress across four key areas:

- **Mood**
- **Awareness**
- **Energy**
- **Constitution**

Users engage with the app through various virtual spaces, each designed to promote different aspects of personal growth.

## 8. Key Features and Functional Requirements

### 8.1 Virtual Mascot ⭐
- Starts as a black sphere with emoticon-based expressions
- Evolves over time based on user actions and progress
- Completes a life cycle in 3 human months
- Responds to user interactions with animations and sounds
- Has customizable appearance options unlocked through progression

### 8.2 Virtual Spaces ⭐
| Space Name | Purpose | Features |
|------------|---------|----------|
| **The Cave** | Introspection and personal growth | - Guided meditation exercises<br>- Mood tracking<br>- Journaling prompts<br>- Self-reflection exercises |
| **Samsara** | Life challenges and skill development | - Daily challenges<br>- Skill-building exercises<br>- Progress tracking |

### 8.3 Point System
Two types of points:
1. **EXP**: Gained by completing challenges, exercises, and daily activities
2. **Coins**: In-game currency for purchasing customizations and power-ups

### 8.4 Mini-Games
1. **Memory Pairs**: Match pairs of cards to improve memory and focus
2. **Simon Says Breath**: Follow breathing patterns to improve mindfulness

### 8.5 User Progression ⭐
- **Daily login rewards** with increasing value for consecutive days
- **Streak bonuses** for maintaining consistent app usage
- **Level system** tied to overall user progress and mascot evolution
- **Achievements** and **badges** for completing specific milestones or challenges
- **Unlockable customization** options for the mascot and virtual spaces

### 8.6 Game Mechanics
1. **Daily Quests**: Set of daily tasks for users to complete, refreshed every 24 hours
2. **Habit Tracking**: Allow users to create and track custom habits
3. **Mood Tracking**: Daily mood check-ins with the option to add notes
4. **Energy System**: Limited daily energy for activities, replenished over time or through in-app purchases
5. **Skill Trees**: Unlock new abilities and features as users progress in specific areas
6. **Seasonal Events**: Time-limited challenges and themes to keep content fresh
7. **Collaborative Challenges**: Group activities that encourage social interaction

### 8.7 User Onboarding Process
1. **Welcome Screen**: Brief introduction to the app's concept and benefits
2. **Character Creation**: Users customize their initial mascot appearance
3. **Guided Tour**: Interactive tutorial showcasing key features and navigation
4. **First Quest**: Simple, guided task to familiarize users with core mechanics
5. **Daily Goal Setting**: Prompt users to set their first personal development goal
6. **Notification Preferences**: Allow users to customize their notification settings
7. **Social Connection**: Option to connect with friends or join the community

### 8.8 Social Features
1. **Friends List**: Add and manage in-app friends
2. **Activity Feed**: View friends' achievements and progress updates
3. **Challenges**: Create or join group challenges with friends or the community
4. **Messaging**: In-app messaging system for communication with friends
5. **Gifting**: Send virtual gifts or encouragement to friends
6. **Leaderboards**: Compare progress with friends or the global community
7. **Community Forums**: Discuss topics related to personal development and share experiences
8. **Mentor/Mentee System**: Match experienced users with newcomers for guidance

### 8.9 Accessibility Features
1. **Color Blind Mode**: Alternative color schemes for color-blind users
2. **Text-to-Speech**: Option to have text read aloud for visually impaired users
3. **Customizable Font Sizes**: Allow users to adjust text size for better readability
4. **Alternative Text**: Provide descriptions for images and icons
5. **Keyboard Navigation**: Enable full app navigation using keyboard shortcuts

### 8.10 Data and Privacy
1. **User Data Encryption**: Ensure all personal data is encrypted at rest and in transit
2. **Privacy Settings**: Granular control over what information is shared publicly or with friends
3. **Data Export**: Allow users to download their personal data
4. **Account Deletion**: Provide option for users to fully delete their account and data
5. **Transparent Data Usage**: Clear explanations of how user data is used within the app

## 9. Technical Requirements

### 9.1 Platform
- **Web application** (**responsive design** for desktop and mobile browsers)

### 9.2 Frontend
- **Framework**: Vue.js with JavaScript
- **Component Library**: Vuetify

### 9.3 Backend
- **Programming Language**: Python
- **Framework**: Django
- **API**: Django REST Framework

### 9.4 Database
- **Primary Database**: PostgreSQL

### 9.5 Deployment
- **Platform**: Heroku

### 9.6 Additional Technologies
- Docker for containerization

## 10. Monetization
- **Free app** with optional **in-app purchases** for **cosmetic items** and power-ups
- **No ads in the initial version to focus on user experience**

## 11. Success Metrics

See `GrowthBuddy_PSA_Success_Metrics.md` for detailed success metrics and KPIs.

## 12. Timeline

See `Plan_Development_Roadmap.md` for the detailed project timeline and milestones.

## 13. Risks and Mitigation Strategies

See `GrowthBuddy_PSA_Risk_Assessment.md` for a comprehensive risk assessment and mitigation plan.

## 14. Market Analysis

### 14.1 Competitors

1. **Habitica**: A habit-building and productivity app that turns your tasks into a game.
   - Strengths: Established user base, RPG-style gameplay
   - Weaknesses: Complex interface, less focus on mental wellness

2. **Fabulous**: A science-based app for building healthy rituals into your life.
   - Strengths: Beautiful design, backed by behavioral science
   - Weaknesses: Less gamification, higher price point

3. **Reflectly**: An AI-powered journaling app for mindfulness and self-reflection.
   - Strengths: AI-driven personalization, focus on mental health
   - Weaknesses: Limited gamification, no virtual pet element

4. **Forest**: An app that helps users stay focused and present by growing virtual trees.
   - Strengths: Simple concept, environmental impact
   - Weaknesses: Limited scope, less comprehensive personal development features

5. **Finch**: A self-care companion app with a virtual bird.
   - Strengths: Gamification, community aspects, emotional engagement
   - Weaknesses: May lack comprehensive personal development features

6. **Amaru**: A virtual pet game integrating self-care practices.
   - Strengths: Daily accountability, gamified mental health habits
   - Weaknesses: Possibly less focus on broader personal growth areas

7. **Calm**: A popular mindfulness and mental well-being app.
   - Strengths: Extensive meditation and relaxation features, well-established brand
   - Weaknesses: No gamification or virtual pet element

8. **Moshi**: A mental health app designed for children.
   - Strengths: Family-friendly, engaging for younger users
   - Weaknesses: Limited appeal to adult users, narrower focus

9. **I Am Sober**: An addiction recovery app with gamification elements.
   - Strengths: Progress tracking, milestone celebrations
   - Weaknesses: Specific focus on addiction recovery, less broad personal development

10. **Laberynthos**: an innovative platform that offers a unique approach to learning and exploring tarot. It combines traditional tarot teachings with modern technology, providing users with interactive and engaging experiences through its mobile app and online resources.
   - Strengths: Stands out with its gamified learning tools that make tarot accessible and engaging for all users. It offers a comprehensive array of educational resources, including courses and interactive exercises, and fosters a strong community where users actively engage and share insights, enhancing the overall learning experience..
   - Weaknesses: Primarily targets tarot enthusiasts, which may limit its broader market appeal. The platform's feature set is somewhat limited, lacking advanced functionalities that could boost user interaction. Additionally, its reliance on a mobile app may not cater to users who prefer desktop or web-based experiences.

### 14.2 **Unique Selling Points** (**USPs**)

1. **Holistic Approach**: GrowEbuddy P.S.A. combines personal development, mental wellness, and gamification in a single app.
2. **Evolving Mascot**: The virtual pet concept provides a tangible representation of personal growth.
3. **Multi-faceted Growt**h: Four key areas (mood, awareness, energy, constitution) offer a comprehensive development experience.
4. **Diverse Virtual Spaces**: Different environments cater to various aspects of personal growth and user preferences.
5. **Community Integration**: Social features foster a supportive environment for users to share experiences and motivate each other.

### 14.3 Market Positioning

GrowEbuddy P.S.A. positions itself as a comprehensive personal development companion that makes self-improvement engaging and rewarding. Our target market includes:

1. **Primary**: Young adults (18-35) seeking a fun, gamified approach to personal growth
2. **Secondary**: Transgenerational users interested in holistic self-improvement

We differentiate ourselves by offering:

- A more engaging and visually appealing experience compared to traditional habit trackers
- A deeper focus on personal development compared to simple virtual pet apps
- A more comprehensive approach to wellness compared to single-focus meditation or productivity apps
- A balance between gamification and serious personal development, suitable for both young adults and older users
- A unique combination of **virtual pet care, habit tracking, and mental wellness** in one app

### 14.4 Market Trends

1. Increasing interest in mental health and wellness apps
2. Growing popularity of gamification in non-game contexts
3. Rising demand for **personalized, AI-driven experiences**
4. Shift towards **holistic approaches** to personal development
5. Increasing use of **mobile apps** for **self-improvement and habit tracking**

### 14.5 Growth Opportunities

1. **Partnerships** with mental health professionals or life coaches to provide expert content
2. **Integration** with **wearable devices** for more accurate tracking of physical activities and sleep
3. Expansion into **corporate wellness programs**
4. Development of **educational resources** and **workshops** based on app principles
5. Creation of a **premium subscription tier** with **advanced features** and **personalized coaching**

This market analysis provides insights into the competitive landscape, highlights our unique selling points, and identifies potential growth opportunities for GrowEbuddy P.S.A.

## 15. Design Guidelines

### 15.1 Visual Style Guide

#### **Color Palette**
- **Primary Colo**r: #4CAF50 (**Green**) - Represents growth and positivity
- **Secondary Color**: #2196F3 (**Blue**) - Represents calmness and trust
- **Accent Color**: #FFC107 (**Amber**) - Represents energy and motivation
- **Background Color**: #FAFAFA (**Light Grey**) - Provides a clean, uncluttered backdrop
- **Text Color**: #212121 (**Dark Grey**) - Ensures readability

Use a **60-30-10 rule** for color distribution: **60% primary/background**, **30% secondary**, and **10% accent colors**.

#### Typography
- **Primary Font**: **Roboto** - A clean, modern sans-serif font for good readability
- **Heading Font**: **Montserrat** - A slightly more distinctive sans-serif for headings
- **Font Sizes**:
  - **H1**: 24px
  - **H2**: 20px
  - **H3**: 18px
  - **Body**: 16px
  - **Small Text**: 14px

Maintain **a line height of 1.5** for optimal readability.

#### Iconography
Use **Material Design icons** for consistency and familiarity. **Custom icons for the mascot and specific game elements** should follow the **same style guidelines for cohesiveness**.

### 15.2 UI Components

Utilize **Vuetify components** for consistency and efficiency. Key components include:
- **Buttons**: Use rounded buttons with clear hover and active states
- **Cards**: For displaying information and interactive elements
- **Bottom Navigation**: For main app navigation on mobile
- **Dialogs**: For important notifications and confirmations
- **Progress Bars**: To visualize user progress and achievements

### 15.3 Layout Guidelines

- Use a **responsive grid system (12 columns)** for flexible layouts across devices
- Maintain **consistent spacing using an 8px grid system**
- Use **card-based design** for organizing content and features
- Implement a **bottom navigation bar for primary navigation on mobile**
- Use a **sidebar navigation for desktop views**

### 15.4 User Experience Principles

1. **Simplicity**: Keep interfaces clean and uncluttered
2. **Consistency**: Maintain consistent design patterns throughout the app
3. **Feedback**: Provide clear feedback for all user actions
4. **Discoverability**: Make features and actions easily discoverable
5. **Efficiency**: Minimize the number of steps required to complete tasks

### 15.5 Accessibility Guidelines

1. **Color Contrast**: Ensure a **minimum contrast ratio** of **4.5:1** for **normal text** and **3:1** for **large text**
2. **Text Alternatives**: Provide alt text for all images and icons
3. **Keyboard Navigation**: Ensure all interactive elements are keyboard accessible
4. **Focus Indicators**: Provide clear visual focus indicators for interactive elements
5. **Scalable Text**: Allow users to **resize text up to 200%** **without loss** of **content or functionality**

### 15.6 Localization Considerations

1. **Text Expansion**: Design layouts to accommodate text expansion for different languages (**allow for up to 40% expansion**)
2. **Cultural Sensitivity**: Use culturally neutral icons and imagery
3. **Date and Time Formats**: Support different date and time formats
4. **Right-to-Left (RTL) Support**: Design layouts that can be mirrored for RTL languages

### 15.7 Mascot Design Guidelines

1. **Simplicity**: Keep the mascot design simple and easily recognizable
2. **Expressiveness**: Design the mascot with a range of expressions to reflect different states and emotions
3. **Scalability**: Ensure the mascot design works well at various sizes
4. **Customization**: Allow for user customization while maintaining the core character of the mascot

### 15.8 Gamification Elements

1. **Progress Visualization**: Use clear, visually appealing methods to show user progress (e.g., progress bars, level indicators)
2. **Rewards**: Design visually attractive rewards and achievements
3. **Challenges**: Create engaging visual representations for challenges and quests
4. **Leaderboards**: Design clean, easy-to-read leaderboards that motivate without overwhelming users

### 15.9 Onboarding Design

1. **Progressive Disclosure**: Introduce features gradually to avoid overwhelming new users
2. **Interactive Tutorials**: Design engaging, interactive tutorials for key features
3. **Contextual Help**: Provide easily accessible help and explanations within the interface

### 15.10 Responsive Design Principles

1. **Mobile-First Approach**: Design for mobile screens first, then adapt for larger screens
2. **Flexible Grids**: Use a flexible grid system that adapts to different screen sizes
3. **Touchable Elements**: Ensure interactive elements are large enough for touch interactions (**minimum 44x44 pixels**)
4. **Adaptive Content**: Adjust content display and hierarchy based on screen size and orientation

These design guidelines provide a comprehensive framework for creating a consistent, accessible, and engaging user experience for GrowEbuddy P.S.A. They should be used in conjunction with the Vuetify component library to ensure a cohesive design across the application.

## 16. Future Enhancements

This section outlines potential future features and enhancements that could be added to GrowEbuddy P.S.A. as the project evolves:

### 16.1 Additional Virtual Spaces
- **The Reflections Biome**: For nature connection and interpersonal relationships, and a social spacee
- **The Void**: For creativity and personal expression

### 16.2 Expanded Point System
- Introduce **Seeds** for **social interactions and community participation**
- Add **Droops** for **daily logins and basic activities**

### 16.3 More Mini-Games
- **Long List**: Memorize and recall lists of items to enhance cognitive skills
- **Infinite Bite Runner**: An endless runner game promoting quick decision-making
- **Story Making**: Create short stories to boost creativity and writing skills

### 16.4 Advanced Technical Features
- Implement caching with Redis for improved performance
- Integrate MongoDB for flexible data storage needs
- Add real-time features using Firebase
- Develop native mobile applications for iOS and Android

### 16.5 Enhanced Monetization
- Implement **a subscription model** with premium features
- Introduce **in-app advertising for free users**

### 16.6 Advanced Analytics and Reporting
- Implement comprehensive user behavior tracking
- Develop detailed performance metrics and KPIs

These future enhancements provide a roadmap for expanding GrowEbuddy P.S.A.'s features and capabilities as the project grows and evolves beyond its initial MVP stage.
