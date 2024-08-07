endpoint_graphql="https://services.cytoid.io/graphql"
endpoint_oldhttpapi="https://services.cytoid.io/profile/$uid/details"
user_info_query_without_any = '''
{
  profile(uid: "$uid") {
    
    bio,
    rating,
    exp{
      basicExp,
      levelExp,
      totalExp,
      currentLevel,
      nextLevelExp,
      currentLevelExp
    }
    activity{
      totalRankedPlays,
      clearedNotes,
      maxCombo,
      averageRankedAccuracy,
      totalRankedScore,
      totalPlayTime
    }
    user {
      collectionsCount
      collections {
        uid
        cover {
          original
        }
        title
        description
        levelCount
        modificationDate
      }
      uid
      registrationDate
      avatar {
        original
      }
    },
    timeseries{
      cumulativeRating,
      cumulativeAccuracy,
      week,
      year,
      accuracy,
      rating,
      count
    }
  }
}

'''

user_info_query_with_recent='''
{
  profile(uid: "$uid") {
    
    bio
    rating
    exp {
      basicExp
      levelExp
      totalExp
      currentLevel
      nextLevelExp
      currentLevelExp
    }
    
    activity {
      totalRankedPlays
      clearedNotes
      maxCombo
      averageRankedAccuracy
      totalRankedScore
      totalPlayTime
    }
    user {
      collectionsCount
      collections {
        uid
        cover {
          original
        }
        title
        description
        levelCount
        modificationDate
      }
      uid
      registrationDate
      avatar {
        original
      }
    }
    timeseries {
      cumulativeRating
      cumulativeAccuracy
      week
      year
      accuracy
      rating
      count
    }
    recentRecords(limit: $recentLimit) {
      date
      chart {
        id
        name
        difficulty
        type
        notesCount
        level {
          bundle {
            musicPreview
            backgroundImage {
              original
            }
          }
        }
      }
      score
      accuracy
      mods
      ranked
      details {
        perfect
        great
        good
        bad
        miss
        maxCombo
      }
      rating
      recentRating
    }
  }
}

'''

b30avg_and_r10avg_query='''
{
  profile(uid:"$uid"){
    recentRecords(limit:10){
      rating
    }
    bestRecords(limit:30){
      rating
    }
  }
}
'''