run_int = int(input("Сколько километроа пробежал спортсмен в первый день? "))
run_max = int(input("Сколько ему нужно пробежать? "))
count = 1
while run_int <= run_max:
            count = count + 1
            run_next = run_int + run_int * 10 / 100  # километров на след.день
            print(count, "-й день - ", round(run_next,2))
            if run_next >= run_max:
                print("Ответ: в", count, "-й день",round(run_next,2))
                break
            else:
                run_int = run_next
                continue



























