
# Game Course Recommender

This is a simplified platform that recommends game development courses to users based on their experience level. 
The system uses Python and Apache Spark to process user and course data, providing personalized recommendations.

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/game-course-recommender.git
```

2. Install dependencies:
```
pip install pyspark pandas scikit-learn
```

## Usage

1. Run the recommender system:
```
python recommender.py
```

2. Enter the user ID when prompted, and the system will recommend relevant courses based on their experience level.

## Data

The system uses two CSV files:

- `users.csv`: Contains user data including user ID, name, and experience level.
- `courses.csv`: Contains course data including course ID, course name, and difficulty level.
