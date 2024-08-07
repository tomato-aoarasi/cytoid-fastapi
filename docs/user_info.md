## user/info

| arguments       | description                                                                 | optional                                        |
|:----------------|:----------------------------------------------------------------------------|-------------------------------------------------|
| uid             | username                                                                    | false                                           |
| recent          | number, range 0-100. The number of recently played songs expected           | true                                            |
| with_bests_info | boolean. if true will reply with best30_avg, recent10_avg                   | true                                            |

###### Tag

* Need Token

#### Example

* `{apiurl}/user/info?uid=tigerhix&recent=2&with_bests_info=true`

###### Return data

```json5
{
    "profile": {
        "bio": "Your humble developer. Feel free to buy me some coffee on [Patreon](https://patreon.com/tigerhix)!",
        "rating": 9.28834925975,
        "exp": {
            "basicExp": 1749687,
            "levelExp": 1144274,
            "totalExp": 2893961,
            "currentLevel": 139,
            "nextLevelExp": 2925950,
            "currentLevelExp": 2884200
        },
        "activity": {
            "totalRankedPlays": 1820,
            "clearedNotes": 1718505,
            "maxCombo": 2421,
            "averageRankedAccuracy": 0.8588158225989011,
            "totalRankedScore": 1473516367,
            "totalPlayTime": 243885.77
        },
        "user": {
            "collectionsCount": 0,
            "collections": [],
            "uid": "tigerhix",
            "registrationDate": "2017-08-12T17:21:02.000Z",
            "avatar": {
                "original": "https://assets.cytoid.io/avatar/3uLhdNIANFgOdvALCFeX5mMtZEBSopaMiXQqqXBcA45nNSr7HEcO5kFdJxmWHQ0"
            }
        },
        "timeseries": [
            {
                "cumulativeRating": 8.64939872872445,
                "cumulativeAccuracy": 0.9672375475206683,
                "week": 10,
                "year": 2018,
                "accuracy": 0.9672375475206683,
                "rating": 8.64939872872445,
                "count": 31
            },
            {
                "部分数据因为过长而删除": "Due to excessive length, a portion has been deleted"
            },
            {
                "cumulativeRating": 7.8245182997678775,
                "cumulativeAccuracy": 0.8622609335583049,
                "week": 34,
                "year": 2021,
                "accuracy": 0.8490163286526998,
                "rating": 6.033068021138509,
                "count": 3
            },
            {
                "cumulativeRating": 7.806703183179442,
                "cumulativeAccuracy": 0.859013088282079,
                "week": 44,
                "year": 2021,
                "accuracy": 0.7604017860159792,
                "rating": 7.265799384692619,
                "count": 58
            },
            {
                "cumulativeRating": 7.806968749428699,
                "cumulativeAccuracy": 0.8588911904578315,
                "week": 47,
                "year": 2021,
                "accuracy": 0.748025119304657,
                "rating": 8.048501253128052,
                "count": 2
            }
        ],
        "recentRecords": [
            {
                "date": "2021-11-22T03:44:11.075Z",
                "chart": {
                    "id": 19358,
                    "name": "E!S!M!RUN!",
                    "difficulty": 15,
                    "type": "extreme",
                    "notesCount": 655,
                    "level": null
                },
                "score": 891985,
                "accuracy": 0.9264438,
                "mods": [],
                "ranked": true,
                "details": {
                    "perfect": 534,
                    "great": 72,
                    "good": 34,
                    "bad": 7,
                    "miss": 8,
                    "maxCombo": 386
                },
                "rating": 9.33150591,
                "recentRating": 0,
                "grade": "B"
            },
            {
                "date": "2021-11-22T03:38:16.950Z",
                "chart": {
                    "id": 19358,
                    "name": "E!S!M!RUN!",
                    "difficulty": 15,
                    "type": "extreme",
                    "notesCount": 655,
                    "level": null
                },
                "score": 198892,
                "accuracy": 0.56960644,
                "mods": [],
                "ranked": true,
                "details": {
                    "perfect": 258,
                    "great": 91,
                    "good": 138,
                    "bad": 76,
                    "miss": 92,
                    "maxCombo": 59
                },
                "rating": 6.76549674,
                "recentRating": 0,
                "grade": "F"
            }
        ],
        "best30_avg": 12.384465679666667,
        "recent10_avg": 9.95650155,
        "grade": {
            "D": 47,
            "MAX": 108,
            "B": 157,
            "SS": 167,
            "F": 327,
            "AA": 636,
            "S": 134,
            "C": 66,
            "SSS": 75,
            "A": 241
        }
    }
}
```
