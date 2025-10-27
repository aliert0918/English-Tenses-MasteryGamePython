import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class TensesGame:
    def __init__(self, root):
        self.root = root
        self.root.title("English Tenses Master")
        self.root.geometry("900x700")
        self.root.configure(bg='#2C3E50')
        
        # Variables
        self.current_tense = ""
        self.current_question_index = 0
        self.score = 0
        self.total_questions = 10
        self.user_answers = []
        
        # Database soal
        self.questions_db = self.create_questions_database()
        
        # Start with main menu
        self.show_main_menu()
    
    def create_questions_database(self):
        """Database soal untuk setiap tenses"""
        return {
            # PRESENT TENSES
            "Simple Present": [
                {
                    "question": "She ___ (go) to school every day.",
                    "options": ["go", "goes", "going", "went"],
                    "answer": "goes",
                    "explanation": "Simple Present dengan subject 'She' menggunakan verb + s/es"
                },
                {
                    "question": "They ___ (play) football on weekends.",
                    "options": ["plays", "play", "playing", "played"],
                    "answer": "play",
                    "explanation": "Simple Present dengan subject 'They' menggunakan verb bentuk dasar"
                },
                {
                    "question": "The sun ___ (rise) in the east.",
                    "options": ["rise", "rises", "rising", "risen"],
                    "answer": "rises",
                    "explanation": "Simple Present untuk fakta umum, subject tunggal + verb-s"
                },
                {
                    "question": "I ___ (not/like) spicy food.",
                    "options": ["don't like", "doesn't like", "not like", "didn't like"],
                    "answer": "don't like",
                    "explanation": "Simple Present negative dengan 'I' menggunakan don't + verb"
                },
                {
                    "question": "___ he ___ (speak) English?",
                    "options": ["Do/speak", "Does/speak", "Does/speaks", "Do/speaks"],
                    "answer": "Does/speak",
                    "explanation": "Simple Present question dengan 'he' menggunakan Does + verb dasar"
                },
                {
                    "question": "Water ___ (boil) at 100 degrees Celsius.",
                    "options": ["boil", "boils", "boiling", "boiled"],
                    "answer": "boils",
                    "explanation": "Simple Present untuk fakta ilmiah"
                },
                {
                    "question": "My parents ___ (work) in a hospital.",
                    "options": ["works", "work", "working", "worked"],
                    "answer": "work",
                    "explanation": "Simple Present dengan subject plural menggunakan verb dasar"
                },
                {
                    "question": "He always ___ (arrive) on time.",
                    "options": ["arrive", "arrives", "arriving", "arrived"],
                    "answer": "arrives",
                    "explanation": "Simple Present dengan frequency adverb 'always'"
                },
                {
                    "question": "Cats ___ (love) fish.",
                    "options": ["love", "loves", "loving", "loved"],
                    "answer": "love",
                    "explanation": "Simple Present dengan subject plural 'Cats'"
                },
                {
                    "question": "She ___ (not/drink) coffee.",
                    "options": ["don't drink", "doesn't drink", "not drinks", "didn't drink"],
                    "answer": "doesn't drink",
                    "explanation": "Simple Present negative dengan subject 'She' menggunakan doesn't"
                }
            ],
            
            "Present Continuous": [
                {
                    "question": "I ___ (study) English right now.",
                    "options": ["study", "am studying", "is studying", "are studying"],
                    "answer": "am studying",
                    "explanation": "Present Continuous: I + am + verb-ing"
                },
                {
                    "question": "They ___ (watch) TV at the moment.",
                    "options": ["is watching", "are watching", "am watching", "watch"],
                    "answer": "are watching",
                    "explanation": "Present Continuous: They + are + verb-ing"
                },
                {
                    "question": "She ___ (not/work) today.",
                    "options": ["isn't working", "aren't working", "not working", "doesn't work"],
                    "answer": "isn't working",
                    "explanation": "Present Continuous negative: She + isn't + verb-ing"
                },
                {
                    "question": "___ you ___ (listen) to me?",
                    "options": ["Are/listening", "Is/listening", "Do/listen", "Are/listen"],
                    "answer": "Are/listening",
                    "explanation": "Present Continuous question: Are + you + verb-ing"
                },
                {
                    "question": "The children ___ (play) in the garden now.",
                    "options": ["is playing", "are playing", "plays", "playing"],
                    "answer": "are playing",
                    "explanation": "Present Continuous dengan subject plural"
                },
                {
                    "question": "Look! It ___ (rain) outside.",
                    "options": ["rains", "is raining", "are raining", "rain"],
                    "answer": "is raining",
                    "explanation": "'Look!' menunjukkan aktivitas yang sedang terjadi sekarang"
                },
                {
                    "question": "My brother ___ (sleep) upstairs.",
                    "options": ["sleeps", "is sleeping", "are sleeping", "sleeping"],
                    "answer": "is sleeping",
                    "explanation": "Present Continuous untuk aktivitas yang sedang berlangsung"
                },
                {
                    "question": "We ___ (have) dinner at the moment.",
                    "options": ["have", "is having", "are having", "having"],
                    "answer": "are having",
                    "explanation": "Present Continuous: We + are + verb-ing"
                },
                {
                    "question": "The teacher ___ (explain) the lesson now.",
                    "options": ["explains", "is explaining", "are explaining", "explaining"],
                    "answer": "is explaining",
                    "explanation": "Present Continuous dengan subject tunggal"
                },
                {
                    "question": "___ he ___ (come) to the party tonight?",
                    "options": ["Is/coming", "Are/coming", "Does/come", "Is/come"],
                    "answer": "Is/coming",
                    "explanation": "Present Continuous untuk rencana masa depan yang sudah pasti"
                }
            ],
            
            "Present Perfect": [
                {
                    "question": "I ___ (finish) my homework.",
                    "options": ["have finished", "has finished", "finished", "am finishing"],
                    "answer": "have finished",
                    "explanation": "Present Perfect: I + have + past participle"
                },
                {
                    "question": "She ___ (live) here for 5 years.",
                    "options": ["have lived", "has lived", "lived", "is living"],
                    "answer": "has lived",
                    "explanation": "Present Perfect dengan 'for' menunjukkan durasi"
                },
                {
                    "question": "They ___ (never/visit) Japan.",
                    "options": ["have never visited", "has never visited", "never visited", "never visit"],
                    "answer": "have never visited",
                    "explanation": "Present Perfect dengan 'never': have + never + past participle"
                },
                {
                    "question": "___ you ever ___ (eat) sushi?",
                    "options": ["Have/eaten", "Has/eaten", "Have/ate", "Did/eat"],
                    "answer": "Have/eaten",
                    "explanation": "Present Perfect question dengan 'ever'"
                },
                {
                    "question": "He ___ (just/arrive) at the airport.",
                    "options": ["have just arrived", "has just arrived", "just arrived", "is just arriving"],
                    "answer": "has just arrived",
                    "explanation": "Present Perfect dengan 'just' untuk kejadian baru saja terjadi"
                },
                {
                    "question": "We ___ (know) each other since 2010.",
                    "options": ["knew", "have known", "has known", "are knowing"],
                    "answer": "have known",
                    "explanation": "Present Perfect dengan 'since' menunjukkan titik waktu mulai"
                },
                {
                    "question": "The movie ___ (already/start).",
                    "options": ["have already started", "has already started", "already started", "already starts"],
                    "answer": "has already started",
                    "explanation": "Present Perfect dengan 'already'"
                },
                {
                    "question": "I ___ (not/see) him today.",
                    "options": ["haven't seen", "hasn't seen", "didn't see", "don't see"],
                    "answer": "haven't seen",
                    "explanation": "Present Perfect negative: haven't + past participle"
                },
                {
                    "question": "She ___ (be) to Paris three times.",
                    "options": ["have been", "has been", "was", "is"],
                    "answer": "has been",
                    "explanation": "Present Perfect untuk pengalaman"
                },
                {
                    "question": "They ___ (work) here since last year.",
                    "options": ["worked", "have worked", "has worked", "are working"],
                    "answer": "have worked",
                    "explanation": "Present Perfect dengan 'since' + waktu spesifik"
                }
            ],
            
            "Present Perfect Continuous": [
                {
                    "question": "I ___ (wait) for 2 hours.",
                    "options": ["have been waiting", "has been waiting", "am waiting", "waited"],
                    "answer": "have been waiting",
                    "explanation": "Present Perfect Continuous: have been + verb-ing"
                },
                {
                    "question": "She ___ (study) English since morning.",
                    "options": ["have been studying", "has been studying", "is studying", "studied"],
                    "answer": "has been studying",
                    "explanation": "Present Perfect Continuous dengan 'since'"
                },
                {
                    "question": "They ___ (play) tennis for an hour.",
                    "options": ["have been playing", "has been playing", "are playing", "played"],
                    "answer": "have been playing",
                    "explanation": "Present Perfect Continuous menunjukkan durasi aktivitas"
                },
                {
                    "question": "How long ___ you ___ (learn) Spanish?",
                    "options": ["have/been learning", "has/been learning", "are/learning", "have/learned"],
                    "answer": "have/been learning",
                    "explanation": "Present Perfect Continuous question dengan 'How long'"
                },
                {
                    "question": "It ___ (rain) all day.",
                    "options": ["has been raining", "have been raining", "is raining", "rained"],
                    "answer": "has been raining",
                    "explanation": "Present Perfect Continuous untuk aktivitas berkelanjutan"
                },
                {
                    "question": "He ___ (not/sleep) well lately.",
                    "options": ["hasn't been sleeping", "haven't been sleeping", "isn't sleeping", "didn't sleep"],
                    "answer": "hasn't been sleeping",
                    "explanation": "Present Perfect Continuous negative"
                },
                {
                    "question": "We ___ (work) on this project since January.",
                    "options": ["have been working", "has been working", "are working", "worked"],
                    "answer": "have been working",
                    "explanation": "Present Perfect Continuous dengan 'since' + bulan"
                },
                {
                    "question": "The baby ___ (cry) for 30 minutes.",
                    "options": ["have been crying", "has been crying", "is crying", "cried"],
                    "answer": "has been crying",
                    "explanation": "Present Perfect Continuous dengan subject tunggal"
                },
                {
                    "question": "___ they ___ (live) here long?",
                    "options": ["Have/been living", "Has/been living", "Are/living", "Have/lived"],
                    "answer": "Have/been living",
                    "explanation": "Present Perfect Continuous question"
                },
                {
                    "question": "My eyes hurt. I ___ (read) for hours.",
                    "options": ["have been reading", "has been reading", "am reading", "read"],
                    "answer": "have been reading",
                    "explanation": "Present Perfect Continuous menunjukkan hasil dari aktivitas berkelanjutan"
                }
            ],
            
            # PAST TENSES
            "Simple Past": [
                {
                    "question": "I ___ (go) to the cinema yesterday.",
                    "options": ["go", "goes", "went", "gone"],
                    "answer": "went",
                    "explanation": "Simple Past dengan time marker 'yesterday'"
                },
                {
                    "question": "She ___ (not/come) to the party last night.",
                    "options": ["didn't come", "doesn't come", "not came", "didn't came"],
                    "answer": "didn't come",
                    "explanation": "Simple Past negative: didn't + verb dasar"
                },
                {
                    "question": "___ you ___ (see) the movie last week?",
                    "options": ["Did/see", "Did/saw", "Do/see", "Have/seen"],
                    "answer": "Did/see",
                    "explanation": "Simple Past question: Did + subject + verb dasar"
                },
                {
                    "question": "They ___ (buy) a new car last month.",
                    "options": ["buy", "buys", "bought", "buying"],
                    "answer": "bought",
                    "explanation": "Simple Past irregular verb: buy → bought"
                },
                {
                    "question": "He ___ (study) hard for the exam.",
                    "options": ["study", "studies", "studied", "studying"],
                    "answer": "studied",
                    "explanation": "Simple Past regular verb: verb + ed"
                },
                {
                    "question": "We ___ (be) at home yesterday.",
                    "options": ["was", "were", "are", "is"],
                    "answer": "were",
                    "explanation": "Simple Past 'to be' dengan subject plural"
                },
                {
                    "question": "The train ___ (leave) 10 minutes ago.",
                    "options": ["leave", "leaves", "left", "leaving"],
                    "answer": "left",
                    "explanation": "Simple Past dengan 'ago'"
                },
                {
                    "question": "I ___ (write) a letter to my friend.",
                    "options": ["write", "writes", "wrote", "written"],
                    "answer": "wrote",
                    "explanation": "Simple Past irregular verb: write → wrote"
                },
                {
                    "question": "___ she ___ (finish) her homework?",
                    "options": ["Did/finish", "Did/finished", "Does/finish", "Has/finished"],
                    "answer": "Did/finish",
                    "explanation": "Simple Past question dengan subject 'she'"
                },
                {
                    "question": "They ___ (not/know) the answer.",
                    "options": ["didn't know", "doesn't know", "not knew", "didn't knew"],
                    "answer": "didn't know",
                    "explanation": "Simple Past negative dengan irregular verb"
                }
            ],
            
            "Past Continuous": [
                {
                    "question": "I ___ (sleep) when you called.",
                    "options": ["was sleeping", "were sleeping", "slept", "am sleeping"],
                    "answer": "was sleeping",
                    "explanation": "Past Continuous: was/were + verb-ing"
                },
                {
                    "question": "They ___ (play) football at 3 PM yesterday.",
                    "options": ["was playing", "were playing", "played", "are playing"],
                    "answer": "were playing",
                    "explanation": "Past Continuous dengan waktu spesifik di masa lalu"
                },
                {
                    "question": "She ___ (not/work) yesterday afternoon.",
                    "options": ["wasn't working", "weren't working", "didn't work", "not working"],
                    "answer": "wasn't working",
                    "explanation": "Past Continuous negative: wasn't + verb-ing"
                },
                {
                    "question": "___ you ___ (study) at 8 PM last night?",
                    "options": ["Were/studying", "Was/studying", "Did/study", "Are/studying"],
                    "answer": "Were/studying",
                    "explanation": "Past Continuous question dengan 'you'"
                },
                {
                    "question": "While I ___ (cook), the phone rang.",
                    "options": ["was cooking", "were cooking", "cooked", "am cooking"],
                    "answer": "was cooking",
                    "explanation": "Past Continuous dengan 'while' untuk aktivitas yang sedang berlangsung"
                },
                {
                    "question": "The children ___ (watch) TV all evening.",
                    "options": ["was watching", "were watching", "watched", "watching"],
                    "answer": "were watching",
                    "explanation": "Past Continuous untuk aktivitas berkelanjutan di masa lalu"
                },
                {
                    "question": "It ___ (rain) when I left home.",
                    "options": ["was raining", "were raining", "rained", "is raining"],
                    "answer": "was raining",
                    "explanation": "Past Continuous untuk latar belakang kejadian"
                },
                {
                    "question": "What ___ he ___ (do) at 10 AM?",
                    "options": ["was/doing", "were/doing", "did/do", "is/doing"],
                    "answer": "was/doing",
                    "explanation": "Past Continuous question dengan 'what'"
                },
                {
                    "question": "We ___ (not/listen) to music.",
                    "options": ["wasn't listening", "weren't listening", "didn't listen", "not listening"],
                    "answer": "weren't listening",
                    "explanation": "Past Continuous negative dengan subject plural"
                },
                {
                    "question": "She ___ (read) a book when I arrived.",
                    "options": ["was reading", "were reading", "read", "reads"],
                    "answer": "was reading",
                    "explanation": "Past Continuous untuk aktivitas yang terganggu"
                }
            ],
            
            "Past Perfect": [
                {
                    "question": "I ___ (finish) my work before he arrived.",
                    "options": ["had finished", "have finished", "finished", "was finishing"],
                    "answer": "had finished",
                    "explanation": "Past Perfect: had + past participle, terjadi sebelum kejadian lain di masa lalu"
                },
                {
                    "question": "She ___ (already/leave) when I got there.",
                    "options": ["had already left", "has already left", "already left", "was already leaving"],
                    "answer": "had already left",
                    "explanation": "Past Perfect dengan 'already'"
                },
                {
                    "question": "They ___ (not/eat) before the movie started.",
                    "options": ["hadn't eaten", "hasn't eaten", "didn't eat", "weren't eating"],
                    "answer": "hadn't eaten",
                    "explanation": "Past Perfect negative: hadn't + past participle"
                },
                {
                    "question": "___ you ___ (see) that movie before?",
                    "options": ["Had/seen", "Have/seen", "Did/see", "Had/saw"],
                    "answer": "Had/seen",
                    "explanation": "Past Perfect question"
                },
                {
                    "question": "After he ___ (study), he took the test.",
                    "options": ["had studied", "has studied", "studied", "was studying"],
                    "answer": "had studied",
                    "explanation": "Past Perfect dengan 'after'"
                },
                {
                    "question": "The train ___ (leave) before we arrived.",
                    "options": ["had left", "has left", "left", "was leaving"],
                    "answer": "had left",
                    "explanation": "Past Perfect menunjukkan urutan kejadian"
                },
                {
                    "question": "I realized I ___ (forget) my keys.",
                    "options": ["had forgotten", "have forgotten", "forgot", "was forgetting"],
                    "answer": "had forgotten",
                    "explanation": "Past Perfect untuk kejadian yang disadari kemudian"
                },
                {
                    "question": "She was tired because she ___ (work) all day.",
                    "options": ["had worked", "has worked", "worked", "was working"],
                    "answer": "had worked",
                    "explanation": "Past Perfect menjelaskan alasan di masa lalu"
                },
                {
                    "question": "They ___ (never/visit) Europe before 2020.",
                    "options": ["had never visited", "have never visited", "never visited", "were never visiting"],
                    "answer": "had never visited",
                    "explanation": "Past Perfect dengan 'never' dan titik waktu"
                },
                {
                    "question": "By the time I arrived, everyone ___ (go) home.",
                    "options": ["had gone", "has gone", "went", "was going"],
                    "answer": "had gone",
                    "explanation": "Past Perfect dengan 'by the time'"
                }
            ],
            
            "Past Perfect Continuous": [
                {
                    "question": "I ___ (wait) for 2 hours when he finally arrived.",
                    "options": ["had been waiting", "have been waiting", "was waiting", "waited"],
                    "answer": "had been waiting",
                    "explanation": "Past Perfect Continuous: had been + verb-ing"
                },
                {
                    "question": "She was tired because she ___ (work) all morning.",
                    "options": ["had been working", "has been working", "was working", "worked"],
                    "answer": "had been working",
                    "explanation": "Past Perfect Continuous menjelaskan durasi sebelum kejadian lain"
                },
                {
                    "question": "They ___ (study) for 3 hours before the test.",
                    "options": ["had been studying", "have been studying", "were studying", "studied"],
                    "answer": "had been studying",
                    "explanation": "Past Perfect Continuous dengan durasi waktu"
                },
                {
                    "question": "How long ___ you ___ (live) there before you moved?",
                    "options": ["had/been living", "have/been living", "were/living", "did/live"],
                    "answer": "had/been living",
                    "explanation": "Past Perfect Continuous question"
                },
                {
                    "question": "It ___ (rain) for hours before it stopped.",
                    "options": ["had been raining", "has been raining", "was raining", "rained"],
                    "answer": "had been raining",
                    "explanation": "Past Perfect Continuous untuk aktivitas berkelanjutan yang berhenti"
                },
                {
                    "question": "He ___ (not/sleep) well before the exam.",
                    "options": ["hadn't been sleeping", "hasn't been sleeping", "wasn't sleeping", "didn't sleep"],
                    "answer": "hadn't been sleeping",
                    "explanation": "Past Perfect Continuous negative"
                },
                {
                    "question": "We ___ (walk) for miles when we found the hotel.",
                    "options": ["had been walking", "have been walking", "were walking", "walked"],
                    "answer": "had been walking",
                    "explanation": "Past Perfect Continuous menunjukkan aktivitas yang berlangsung lama"
                },
                {
                    "question": "The ground was wet. It ___ (rain).",
                    "options": ["had been raining", "has been raining", "was raining", "rained"],
                    "answer": "had been raining",
                    "explanation": "Past Perfect Continuous menunjukkan bukti hasil aktivitas"
                },
                {
                    "question": "___ they ___ (wait) long before you arrived?",
                    "options": ["Had/been waiting", "Have/been waiting", "Were/waiting", "Did/wait"],
                    "answer": "Had/been waiting",
                    "explanation": "Past Perfect Continuous question"
                },
                {
                    "question": "She ___ (teach) for 10 years before she retired.",
                    "options": ["had been teaching", "has been teaching", "was teaching", "taught"],
                    "answer": "had been teaching",
                    "explanation": "Past Perfect Continuous untuk karir/aktivitas jangka panjang"
                }
            ],
            
            # FUTURE TENSES
            "Simple Future": [
                {
                    "question": "I ___ (go) to Paris next month.",
                    "options": ["will go", "go", "going", "went"],
                    "answer": "will go",
                    "explanation": "Simple Future: will + verb dasar"
                },
                {
                    "question": "She ___ (not/come) to the party tomorrow.",
                    "options": ["won't come", "doesn't come", "not come", "didn't come"],
                    "answer": "won't come",
                    "explanation": "Simple Future negative: won't + verb dasar"
                },
                {
                    "question": "___ you ___ (help) me with this?",
                    "options": ["Will/help", "Do/help", "Are/helping", "Will/helps"],
                    "answer": "Will/help",
                    "explanation": "Simple Future question: Will + subject + verb dasar"
                },
                {
                    "question": "They ___ (arrive) at 8 PM.",
                    "options": ["will arrive", "arrive", "arriving", "arrived"],
                    "answer": "will arrive",
                    "explanation": "Simple Future untuk rencana/prediksi"
                },
                {
                    "question": "I think it ___ (rain) tomorrow.",
                    "options": ["will rain", "rains", "is raining", "rained"],
                    "answer": "will rain",
                    "explanation": "Simple Future dengan 'think' untuk prediksi"
                },
                {
                    "question": "He ___ (be) 30 years old next year.",
                    "options": ["will be", "is", "was", "being"],
                    "answer": "will be",
                    "explanation": "Simple Future dengan 'be'"
                },
                {
                    "question": "We ___ (not/forget) your help.",
                    "options": ["won't forget", "don't forget", "not forget", "didn't forget"],
                    "answer": "won't forget",
                    "explanation": "Simple Future negative untuk janji"
                },
                {
                    "question": "___ they ___ (come) to the wedding?",
                    "options": ["Will/come", "Do/come", "Are/coming", "Will/comes"],
                    "answer": "Will/come",
                    "explanation": "Simple Future question"
                },
                {
                    "question": "The meeting ___ (start) at 10 AM.",
                    "options": ["will start", "starts", "starting", "started"],
                    "answer": "will start",
                    "explanation": "Simple Future untuk jadwal yang akan datang"
                },
                {
                    "question": "I promise I ___ (call) you later.",
                    "options": ["will call", "call", "calling", "called"],
                    "answer": "will call",
                    "explanation": "Simple Future untuk janji"
                }
            ],
            
            "Future Continuous": [
                {
                    "question": "I ___ (work) at 3 PM tomorrow.",
                    "options": ["will be working", "will work", "am working", "work"],
                    "answer": "will be working",
                    "explanation": "Future Continuous: will be + verb-ing"
                },
                {
                    "question": "They ___ (travel) to Japan next week.",
                    "options": ["will be traveling", "will travel", "are traveling", "travel"],
                    "answer": "will be traveling",
                    "explanation": "Future Continuous untuk aktivitas yang akan sedang berlangsung"
                },
                {
                    "question": "She ___ (not/sleep) at midnight.",
                    "options": ["won't be sleeping", "won't sleep", "isn't sleeping", "doesn't sleep"],
                    "answer": "won't be sleeping",
                    "explanation": "Future Continuous negative: won't be + verb-ing"
                },
                {
                    "question": "___ you ___ (use) your car tomorrow?",
                    "options": ["Will/be using", "Will/use", "Are/using", "Do/use"],
                    "answer": "Will/be using",
                    "explanation": "Future Continuous question"
                },
                {
                    "question": "At this time tomorrow, I ___ (fly) to London.",
                    "options": ["will be flying", "will fly", "am flying", "fly"],
                    "answer": "will be flying",
                    "explanation": "Future Continuous dengan waktu spesifik di masa depan"
                },
                {
                    "question": "We ___ (have) dinner at 7 PM.",
                    "options": ["will be having", "will have", "are having", "have"],
                    "answer": "will be having",
                    "explanation": "Future Continuous untuk aktivitas terjadwal"
                },
                {
                    "question": "He ___ (study) all night for the exam.",
                    "options": ["will be studying", "will study", "is studying", "studies"],
                    "answer": "will be studying",
                    "explanation": "Future Continuous untuk durasi aktivitas di masa depan"
                },
                {
                    "question": "___ they ___ (wait) for us?",
                    "options": ["Will/be waiting", "Will/wait", "Are/waiting", "Do/wait"],
                    "answer": "Will/be waiting",
                    "explanation": "Future Continuous question"
                },
                {
                    "question": "The sun ___ (shine) tomorrow morning.",
                    "options": ["will be shining", "will shine", "is shining", "shines"],
                    "answer": "will be shining",
                    "explanation": "Future Continuous untuk prediksi cuaca"
                },
                {
                    "question": "I ___ (not/work) next Monday.",
                    "options": ["won't be working", "won't work", "am not working", "don't work"],
                    "answer": "won't be working",
                    "explanation": "Future Continuous negative untuk rencana"
                }
            ],
            
            "Future Perfect": [
                {
                    "question": "By next year, I ___ (graduate) from university.",
                    "options": ["will have graduated", "will graduate", "have graduated", "graduated"],
                    "answer": "will have graduated",
                    "explanation": "Future Perfect: will have + past participle"
                },
                {
                    "question": "She ___ (finish) the project by Friday.",
                    "options": ["will have finished", "will finish", "has finished", "finishes"],
                    "answer": "will have finished",
                    "explanation": "Future Perfect dengan deadline 'by Friday'"
                },
                {
                    "question": "They ___ (not/arrive) by 8 PM.",
                    "options": ["won't have arrived", "won't arrive", "haven't arrived", "don't arrive"],
                    "answer": "won't have arrived",
                    "explanation": "Future Perfect negative: won't have + past participle"
                },
                {
                    "question": "___ you ___ (complete) the work by tomorrow?",
                    "options": ["Will/have completed", "Will/complete", "Have/completed", "Do/complete"],
                    "answer": "Will/have completed",
                    "explanation": "Future Perfect question"
                },
                {
                    "question": "By 2025, he ___ (work) here for 10 years.",
                    "options": ["will have worked", "will work", "has worked", "works"],
                    "answer": "will have worked",
                    "explanation": "Future Perfect untuk durasi hingga titik waktu tertentu"
                },
                {
                    "question": "The movie ___ (start) by the time we arrive.",
                    "options": ["will have started", "will start", "has started", "starts"],
                    "answer": "will have started",
                    "explanation": "Future Perfect dengan 'by the time'"
                },
                {
                    "question": "I ___ (read) 50 books by the end of this year.",
                    "options": ["will have read", "will read", "have read", "read"],
                    "answer": "will have read",
                    "explanation": "Future Perfect untuk target pencapaian"
                },
                {
                    "question": "They ___ (not/leave) before we get there.",
                    "options": ["won't have left", "won't leave", "haven't left", "don't leave"],
                    "answer": "won't have left",
                    "explanation": "Future Perfect negative dengan 'before'"
                },
                {
                    "question": "By midnight, she ___ (sleep) for 8 hours.",
                    "options": ["will have slept", "will sleep", "has slept", "sleeps"],
                    "answer": "will have slept",
                    "explanation": "Future Perfect untuk durasi aktivitas"
                },
                {
                    "question": "___ he ___ (finish) his homework by dinner time?",
                    "options": ["Will/have finished", "Will/finish", "Has/finished", "Does/finish"],
                    "answer": "Will/have finished",
                    "explanation": "Future Perfect question dengan waktu spesifik"
                }
            ],
            
            "Future Perfect Continuous": [
                {
                    "question": "By next month, I ___ (work) here for 2 years.",
                    "options": ["will have been working", "will be working", "have been working", "work"],
                    "answer": "will have been working",
                    "explanation": "Future Perfect Continuous: will have been + verb-ing"
                },
                {
                    "question": "She ___ (study) for 5 hours by midnight.",
                    "options": ["will have been studying", "will be studying", "has been studying", "studies"],
                    "answer": "will have been studying",
                    "explanation": "Future Perfect Continuous untuk durasi hingga waktu tertentu"
                },
                {
                    "question": "They ___ (not/wait) long when we arrive.",
                    "options": ["won't have been waiting", "won't be waiting", "haven't been waiting", "aren't waiting"],
                    "answer": "won't have been waiting",
                    "explanation": "Future Perfect Continuous negative"
                },
                {
                    "question": "How long ___ you ___ (learn) English by next year?",
                    "options": ["will/have been learning", "will/be learning", "have/been learning", "are/learning"],
                    "answer": "will/have been learning",
                    "explanation": "Future Perfect Continuous question dengan 'How long'"
                },
                {
                    "question": "By 6 PM, we ___ (drive) for 10 hours.",
                    "options": ["will have been driving", "will be driving", "have been driving", "drive"],
                    "answer": "will have been driving",
                    "explanation": "Future Perfect Continuous untuk aktivitas berkelanjutan"
                },
                {
                    "question": "He ___ (teach) for 30 years by the time he retires.",
                    "options": ["will have been teaching", "will be teaching", "has been teaching", "teaches"],
                    "answer": "will have been teaching",
                    "explanation": "Future Perfect Continuous untuk karir jangka panjang"
                },
                {
                    "question": "The children ___ (play) for hours by bedtime.",
                    "options": ["will have been playing", "will be playing", "have been playing", "play"],
                    "answer": "will have been playing",
                    "explanation": "Future Perfect Continuous dengan aktivitas anak-anak"
                },
                {
                    "question": "___ they ___ (travel) for long when they arrive?",
                    "options": ["Will/have been traveling", "Will/be traveling", "Have/been traveling", "Are/traveling"],
                    "answer": "Will/have been traveling",
                    "explanation": "Future Perfect Continuous question"
                },
                {
                    "question": "By December, it ___ (rain) for 3 months.",
                    "options": ["will have been raining", "will be raining", "has been raining", "rains"],
                    "answer": "will have been raining",
                    "explanation": "Future Perfect Continuous untuk fenomena alam"
                },
                {
                    "question": "I ___ (not/sleep) well for weeks by the exam day.",
                    "options": ["won't have been sleeping", "won't be sleeping", "haven't been sleeping", "don't sleep"],
                    "answer": "won't have been sleeping",
                    "explanation": "Future Perfect Continuous negative untuk kondisi berkelanjutan"
                }
            ]
        }
    
    def show_main_menu(self):
        """Tampilkan menu utama"""
        self.clear_window()
        
        # Title
        title_frame = tk.Frame(self.root, bg='#2C3E50')
        title_frame.pack(pady=50)
        
        title_label = tk.Label(
            title_frame,
            text="🎓 ENGLISH TENSES MASTER 🎓",
            font=('Arial', 32, 'bold'),
            fg='#ECF0F1',
            bg='#2C3E50'
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Master Your English Grammar Skills",
            font=('Arial', 14),
            fg='#BDC3C7',
            bg='#2C3E50'
        )
        subtitle_label.pack()
        
        # Buttons
        button_frame = tk.Frame(self.root, bg='#2C3E50')
        button_frame.pack(pady=30)
        
        play_btn = tk.Button(
            button_frame,
            text="🎮 PLAY",
            font=('Arial', 18, 'bold'),
            bg='#27AE60',
            fg='white',
            width=20,
            height=2,
            command=self.show_tense_selection,
            cursor='hand2'
        )
        play_btn.pack(pady=10)
        
        instructions_btn = tk.Button(
            button_frame,
            text="📖 INSTRUCTIONS",
            font=('Arial', 18, 'bold'),
            bg='#3498DB',
            fg='white',
            width=20,
            height=2,
            command=self.show_instructions,
            cursor='hand2'
        )
        instructions_btn.pack(pady=10)
        
        exit_btn = tk.Button(
            button_frame,
            text="🚪 EXIT",
            font=('Arial', 18, 'bold'),
            bg='#E74C3C',
            fg='white',
            width=20,
            height=2,
            command=self.root.quit,
            cursor='hand2'
        )
        exit_btn.pack(pady=10)
    
    def show_instructions(self):
        """Tampilkan instruksi permainan"""
        self.clear_window()
        
        # Title
        title_label = tk.Label(
            self.root,
            text="📖 GAME INSTRUCTIONS",
            font=('Arial', 24, 'bold'),
            fg='#ECF0F1',
            bg='#2C3E50'
        )
        title_label.pack(pady=20)
        
        # Instructions frame with scrollbar
        inst_frame = tk.Frame(self.root, bg='#34495E')
        inst_frame.pack(padx=50, pady=20, fill='both', expand=True)
        
        instructions_text = """
        🎯 OBJECTIVE:
        Master all 12 English tenses through interactive exercises!
        
        📚 TENSES COVERED:
        
        PRESENT TENSES:
        • Simple Present - Regular actions and facts
        • Present Continuous - Ongoing actions now
        • Present Perfect - Past actions with present relevance
        • Present Perfect Continuous - Duration until now
        
        PAST TENSES:
        • Simple Past - Completed past actions
        • Past Continuous - Ongoing past actions
        • Past Perfect - Earlier past actions
        • Past Perfect Continuous - Duration before past moment
        
        FUTURE TENSES:
        • Simple Future - Future predictions/plans
        • Future Continuous - Ongoing future actions
        • Future Perfect - Completed before future time
        • Future Perfect Continuous - Duration before future time
        
        🎮 HOW TO PLAY:
        1. Click PLAY from the main menu
        2. Select a tense category (Present/Past/Future)
        3. Choose specific tense to practice
        4. Answer 10 questions per tense
        5. Get instant feedback and explanations
        6. Track your score and progress
        
        💡 TIPS:
        • Read each sentence carefully
        • Look for time markers (yesterday, tomorrow, etc.)
        • Pay attention to the subject (I/you/he/she/it/we/they)
        • Learn from the explanations provided
        
        🏆 SCORING:
        • Each correct answer: 10 points
        • Perfect score: 100 points
        • Try to master all 12 tenses!
        """
        
        inst_text = tk.Text(
            inst_frame,
            font=('Arial', 12),
            fg='#ECF0F1',
            bg='#34495E',
            wrap='word',
            padx=20,
            pady=20
        )
        inst_text.pack(fill='both', expand=True)
        inst_text.insert('1.0', instructions_text)
        inst_text.config(state='disabled')
        
        # Back button
        back_btn = tk.Button(
            self.root,
            text="← BACK TO MENU",
            font=('Arial', 14, 'bold'),
            bg='#95A5A6',
            fg='white',
            command=self.show_main_menu,
            cursor='hand2'
        )
        back_btn.pack(pady=20)
    
    def show_tense_selection(self):
        """Tampilkan menu pemilihan tenses"""
        self.clear_window()
        
        # Title
        title_label = tk.Label(
            self.root,
            text="SELECT TENSE CATEGORY",
            font=('Arial', 24, 'bold'),
            fg='#ECF0F1',
            bg='#2C3E50'
        )
        title_label.pack(pady=30)
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#2C3E50')
        main_frame.pack(expand=True, fill='both', padx=50, pady=20)
        
        # Tense categories
        categories = {
            "PRESENT TENSES": {
                "color": "#27AE60",
                "tenses": ["Simple Present", "Present Continuous", 
                          "Present Perfect", "Present Perfect Continuous"]
            },
            "PAST TENSES": {
                "color": "#E67E22",
                "tenses": ["Simple Past", "Past Continuous", 
                          "Past Perfect", "Past Perfect Continuous"]
            },
            "FUTURE TENSES": {
                "color": "#3498DB",
                "tenses": ["Simple Future", "Future Continuous", 
                          "Future Perfect", "Future Perfect Continuous"]
            }
        }
        
        for category, info in categories.items():
            # Category frame
            cat_frame = tk.LabelFrame(
                main_frame,
                text=category,
                font=('Arial', 16, 'bold'),
                fg='white',
                bg=info['color'],
                padx=20,
                pady=15
            )
            cat_frame.pack(fill='x', pady=15)
            
            # Tense buttons
            btn_frame = tk.Frame(cat_frame, bg=info['color'])
            btn_frame.pack()
            
            for i, tense in enumerate(info['tenses']):
                if i % 2 == 0:
                    row_frame = tk.Frame(btn_frame, bg=info['color'])
                    row_frame.pack()
                
                tense_btn = tk.Button(
                    row_frame,
                    text=tense,
                    font=('Arial', 12),
                    bg='white',
                    fg=info['color'],
                    width=25,
                    height=2,
                    command=lambda t=tense: self.start_quiz(t),
                    cursor='hand2'
                )
                tense_btn.pack(side='left', padx=5, pady=5)
        
        # Back button
        back_btn = tk.Button(
            self.root,
            text="← BACK TO MENU",
            font=('Arial', 14, 'bold'),
            bg='#95A5A6',
            fg='white',
            command=self.show_main_menu,
            cursor='hand2'
        )
        back_btn.pack(pady=20)
    
    def start_quiz(self, tense):
        """Mulai quiz untuk tense yang dipilih"""
        self.current_tense = tense
        self.current_question_index = 0
        self.score = 0
        self.user_answers = []
        self.show_question()
    
    def show_question(self):
        """Tampilkan pertanyaan"""
        self.clear_window()
        
        if self.current_question_index >= self.total_questions:
            self.show_results()
            return
        
        question_data = self.questions_db[self.current_tense][self.current_question_index]
        
        # Header
        header_frame = tk.Frame(self.root, bg='#34495E')
        header_frame.pack(fill='x', padx=20, pady=10)
        
        tense_label = tk.Label(
            header_frame,
            text=f"📚 {self.current_tense}",
            font=('Arial', 18, 'bold'),
            fg='#ECF0F1',
            bg='#34495E'
        )
        tense_label.pack(side='left', padx=20)
        
        progress_label = tk.Label(
            header_frame,
            text=f"Question {self.current_question_index + 1}/{self.total_questions}",
            font=('Arial', 14),
            fg='#BDC3C7',
            bg='#34495E'
        )
        progress_label.pack(side='right', padx=20)
        
        # Progress bar
        progress_frame = tk.Frame(self.root, bg='#2C3E50')
        progress_frame.pack(fill='x', padx=50, pady=10)
        
        progress = (self.current_question_index / self.total_questions) * 100
        progress_bar = ttk.Progressbar(
            progress_frame,
            length=800,
            value=progress,
            style='TProgressbar'
        )
        progress_bar.pack()
        
        # Question
        question_frame = tk.Frame(self.root, bg='#ECF0F1', relief='raised', bd=2)
        question_frame.pack(padx=50, pady=30, fill='x')
        
        question_label = tk.Label(
            question_frame,
            text=question_data['question'],
            font=('Arial', 18),
            bg='#ECF0F1',
            fg='#2C3E50',
            wraplength=700,
            pady=30
        )
        question_label.pack()
        
        # Options
        options_frame = tk.Frame(self.root, bg='#2C3E50')
        options_frame.pack(pady=20)
        
        self.selected_option = tk.StringVar()
        
        for i, option in enumerate(question_data['options']):
            option_btn = tk.Radiobutton(
                options_frame,
                text=option,
                variable=self.selected_option,
                value=option,
                font=('Arial', 14),
                bg='#3498DB',
                fg='white',
                selectcolor='#2980B9',
                activebackground='#2980B9',
                width=30,
                pady=10,
                indicatoron=0,
                cursor='hand2'
            )
            option_btn.pack(pady=5)
        
        # Submit button
        submit_btn = tk.Button(
            self.root,
            text="SUBMIT ANSWER",
            font=('Arial', 14, 'bold'),
            bg='#27AE60',
            fg='white',
            command=self.check_answer,
            cursor='hand2',
            width=20,
            height=2
        )
        submit_btn.pack(pady=20)
    
    def check_answer(self):
        """Periksa jawaban dan tampilkan feedback"""
        if not self.selected_option.get():
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        
        question_data = self.questions_db[self.current_tense][self.current_question_index]
        user_answer = self.selected_option.get()
        correct_answer = question_data['answer']
        
        # Save answer
        self.user_answers.append({
            'question': question_data['question'],
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'is_correct': user_answer == correct_answer
        })
        
        if user_answer == correct_answer:
            self.score += 10
            self.show_feedback(True, question_data['explanation'])
        else:
            self.show_feedback(False, question_data['explanation'])
    
    def show_feedback(self, is_correct, explanation):
        """Tampilkan feedback untuk jawaban"""
        feedback_window = tk.Toplevel(self.root)
        feedback_window.title("Answer Feedback")
        feedback_window.geometry("600x400")
        feedback_window.configure(bg='#2C3E50')
        
        # Result icon and text
        if is_correct:
            result_text = "✅ CORRECT!"
            result_color = "#27AE60"
        else:
            result_text = "❌ INCORRECT"
            result_color = "#E74C3C"
        
        result_label = tk.Label(
            feedback_window,
            text=result_text,
            font=('Arial', 24, 'bold'),
            fg=result_color,
            bg='#2C3E50'
        )
        result_label.pack(pady=30)
        
        # Explanation
        exp_frame = tk.Frame(feedback_window, bg='#34495E', relief='raised', bd=2)
        exp_frame.pack(padx=30, pady=20, fill='both', expand=True)
        
        exp_title = tk.Label(
            exp_frame,
            text="💡 Explanation:",
            font=('Arial', 14, 'bold'),
            fg='#F39C12',
            bg='#34495E'
        )
        exp_title.pack(pady=10)
        
        exp_text = tk.Label(
            exp_frame,
            text=explanation,
            font=('Arial', 12),
            fg='#ECF0F1',
            bg='#34495E',
            wraplength=500,
            justify='left'
        )
        exp_text.pack(pady=10, padx=20)
        
        # Next button
        next_btn = tk.Button(
            feedback_window,
            text="NEXT QUESTION →",
            font=('Arial', 14, 'bold'),
            bg='#3498DB',
            fg='white',
            command=lambda: self.next_question(feedback_window),
            cursor='hand2'
        )
        next_btn.pack(pady=20)
    
    def next_question(self, feedback_window):
        """Lanjut ke pertanyaan berikutnya"""
        feedback_window.destroy()
        self.current_question_index += 1
        self.show_question()
    
    def show_results(self):
        """Tampilkan hasil akhir"""
        self.clear_window()
        
        # Title
        title_label = tk.Label(
            self.root,
            text="🏆 QUIZ COMPLETED! 🏆",
            font=('Arial', 28, 'bold'),
            fg='#F1C40F',
            bg='#2C3E50'
        )
        title_label.pack(pady=30)
        
        # Score
        score_frame = tk.Frame(self.root, bg='#34495E', relief='raised', bd=3)
        score_frame.pack(pady=20)
        
        score_label = tk.Label(
            score_frame,
            text=f"Your Score: {self.score}/100",
            font=('Arial', 24, 'bold'),
            fg='#ECF0F1',
            bg='#34495E',
            padx=50,
            pady=20
        )
        score_label.pack()
        
        # Performance message
        if self.score >= 80:
            msg = "🌟 Excellent! You're a tenses master!"
            color = "#27AE60"
        elif self.score >= 60:
            msg = "👍 Good job! Keep practicing!"
            color = "#F39C12"
        else:
            msg = "📚 Keep studying! You'll get better!"
            color = "#E74C3C"
        
        msg_label = tk.Label(
            self.root,
            text=msg,
            font=('Arial', 18),
            fg=color,
            bg='#2C3E50'
        )
        msg_label.pack(pady=20)
        
        # Summary
        summary_frame = tk.Frame(self.root, bg='#2C3E50')
        summary_frame.pack(pady=20)
        
        correct_count = sum(1 for ans in self.user_answers if ans['is_correct'])
        
        summary_text = f"""
        📊 Summary:
        • Tense: {self.current_tense}
        • Correct Answers: {correct_count}/{self.total_questions}
        • Incorrect Answers: {self.total_questions - correct_count}/{self.total_questions}
        • Completion Time: {datetime.now().strftime('%H:%M:%S')}
        """
        
        summary_label = tk.Label(
            summary_frame,
            text=summary_text,
            font=('Arial', 14),
            fg='#BDC3C7',
            bg='#2C3E50',
            justify='left'
        )
        summary_label.pack()
        
        # Buttons
        btn_frame = tk.Frame(self.root, bg='#2C3E50')
        btn_frame.pack(pady=30)
        
        review_btn = tk.Button(
            btn_frame,
            text="📝 REVIEW ANSWERS",
            font=('Arial', 14, 'bold'),
            bg='#9B59B6',
            fg='white',
            command=self.show_review,
            cursor='hand2',
            width=18
        )
        review_btn.pack(side='left', padx=10)
        
        retry_btn = tk.Button(
            btn_frame,
            text="🔄 TRY AGAIN",
            font=('Arial', 14, 'bold'),
            bg='#3498DB',
            fg='white',
            command=lambda: self.start_quiz(self.current_tense),
            cursor='hand2',
            width=18
        )
        retry_btn.pack(side='left', padx=10)
        
        menu_btn = tk.Button(
            btn_frame,
            text="🏠 MAIN MENU",
            font=('Arial', 14, 'bold'),
            bg='#95A5A6',
            fg='white',
            command=self.show_main_menu,
            cursor='hand2',
            width=18
        )
        menu_btn.pack(side='left', padx=10)
    
    def show_review(self):
        """Tampilkan review jawaban"""
        review_window = tk.Toplevel(self.root)
        review_window.title("Review Answers")
        review_window.geometry("800x600")
        review_window.configure(bg='#2C3E50')
        
        # Title
        title_label = tk.Label(
            review_window,
            text="📝 ANSWER REVIEW",
            font=('Arial', 20, 'bold'),
            fg='#ECF0F1',
            bg='#2C3E50'
        )
        title_label.pack(pady=20)
        
        # Scrollable frame for answers
        canvas = tk.Canvas(review_window, bg='#34495E')
        scrollbar = tk.Scrollbar(review_window, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#34495E')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Display each answer
        for i, answer in enumerate(self.user_answers, 1):
            ans_frame = tk.Frame(scrollable_frame, bg='#2C3E50', relief='raised', bd=1)
            ans_frame.pack(fill='x', padx=20, pady=10)
            
            # Question number and status
            if answer['is_correct']:
                status = "✅"
                color = "#27AE60"
            else:
                status = "❌"
                color = "#E74C3C"
            
            header = tk.Label(
                ans_frame,
                text=f"Question {i} {status}",
                font=('Arial', 12, 'bold'),
                fg=color,
                bg='#2C3E50'
            )
            header.pack(anchor='w', padx=10, pady=5)
            
            # Question
            q_label = tk.Label(
                ans_frame,
                text=f"Q: {answer['question']}",
                font=('Arial', 11),
                fg='#ECF0F1',
                bg='#2C3E50',
                wraplength=700,
                justify='left'
            )
            q_label.pack(anchor='w', padx=20, pady=2)
            
            # Your answer
            your_ans = tk.Label(
                ans_frame,
                text=f"Your answer: {answer['user_answer']}",
                font=('Arial', 11),
                fg='#3498DB' if answer['is_correct'] else '#E74C3C',
                bg='#2C3E50'
            )
            your_ans.pack(anchor='w', padx=20, pady=2)
            
            # Correct answer (if wrong)
            if not answer['is_correct']:
                correct_ans = tk.Label(
                    ans_frame,
                    text=f"Correct answer: {answer['correct_answer']}",
                    font=('Arial', 11, 'bold'),
                    fg='#27AE60',
                    bg='#2C3E50'
                )
                correct_ans.pack(anchor='w', padx=20, pady=2)
        
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Close button
        close_btn = tk.Button(
            review_window,
            text="CLOSE",
            font=('Arial', 12, 'bold'),
            bg='#95A5A6',
            fg='white',
            command=review_window.destroy,
            cursor='hand2'
        )
        close_btn.pack(pady=10)
    
    def clear_window(self):
        """Hapus semua widget dari window"""
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = TensesGame(root)
    root.mainloop()

if __name__ == "__main__":

    main()
