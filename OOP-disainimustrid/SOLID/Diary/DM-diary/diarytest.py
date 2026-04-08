from diary import Diary
from diary_persistence import DiaryPersistence
from diary_statistics import DiaryStatistics

# testimiseks
if __name__ == '__main__':
    d = Diary()

    # lisab kaks sissekannet
    d.add_entry("Täna oli ilus ilm ja me lähme sõpradega kiikuma.")
    d.add_entry("Õppisin programmeerimist disaini mustrite tunnis.")
    
    # Prindib päeviku sisu
    print("Päeviku sisu:")
    print(d)
    print()
    
    # Kasutab DiaryPersistence klassi salvestamiseks
    DiaryPersistence.save(d, "diary.txt")
    
    # Kasutab DiaryStatistics klassi statistika arvutamiseks
    DiaryStatistics.print_statistics(d)
    print()
    
    # testib päeviku sissekannete kustutamist
    d.del_entry(0)
    print("Päeviku sisu pärast kustutamist:")
    print(d)
    print()
    
    # Salvestab jälle
    DiaryPersistence.save(d, "diary.txt")

