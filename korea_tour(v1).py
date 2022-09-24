from search import *

if __name__=="__main__" :
    korea_map = UndirectedGraph(dict(
    Seoul=dict(Sejong=150, Yeoju=80),
    Yeoju=dict(Wonju=39, Sangju=135),
    Wonju=dict(Kangnung=127, Euisung=157),
    Cheonan=dict(Sejong=40),
    Sejong=dict(Daejeon=36, Sangju=96),
    Sangju=dict(Euisung=67, Kumi=54),
    Daejeon=dict(Kumi=110),
    Euisung=dict(Youngduk=83,Daeku=78),
    Kumi=dict(Daeku=49),
    Daeku=dict(Gyeongju=74, Pusan=109),
    Pusan=dict(Gyeongju=80)
    ))

    print ("Korea Map Infomation: ")
    for city in korea_map.graph_dict.items(): print(city)
    print ()

    kor_problem = GraphProblem('Seoul', 'Pusan', korea_map)
   
    print ("Search Strategy : Breadth-first Tree Search")
    seoul_pusan_sol = breadth_first_tree_search(kor_problem)
 
    print ("Seoul to Pusan Tour: ", seoul_pusan_sol.solution())
    print ("Seoul to Pusan Total Distance: ", seoul_pusan_sol.path_cost)
    print ()
   
    print ("Search Strategy : Depth-first Graph Search")
    seoul_pusan_sol = depth_first_graph_search(kor_problem)

    print ("Seoul to Pusan Tour: ", seoul_pusan_sol.solution())
    print ("Seoul to Pusan Total Distance: ", seoul_pusan_sol.path_cost)
    print ()
    """
    print ("Search Strategy : Depth-first Tree Search")
    seoul_pusan_sol = depth_first_tree_search(kor_problem)
   
    print ("Seoul to Pusan Tour: ", seoul_pusan_sol.solution())
    print ("Seoul to Pusan Total Distance: ", seoul_pusan_sol.path_cost)
    print ()
    """
    print ("Search Strategy : Uniform-Cost Search")
    seoul_pusan_sol = uniform_cost_search(kor_problem)
   
    print ("Seoul to Pusan Tour: ", seoul_pusan_sol.solution())
    print ("Seoul to Pusan Total Distance: ", seoul_pusan_sol.path_cost)
    print () 
