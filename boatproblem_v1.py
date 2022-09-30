# 선교인과 식인종

from search import *

class BoatProblem(Problem):
    def __init__(self, initState):
        initTupleState = tuple(initState)
        Problem.__init__https://github.com/leedahye2001/aima-python.git(self, initTupleState)

    def actions(self, state):
        acts = []
        # 하나의 동작은 x명의 선교사와 y명의 식인종을 보트에 태우고 간다는 의미를 담고 있다.
        # 즉, 보트 승선인원 (x, y)의 모든 가능한 조합들이 가능한 모든 동작들이 된다.
        # 여기서, x는 선교사의 수, y는 식인종의 수이다. 
        for x in (0, 1, 2) : 
            for y in (0, 1, 2) :
                action = (x, y)
                if state[4] == 0 :
                    xx = x; yy = y
                else:
                    xx = -x; yy = -y
                nextState = (
                    state[0] - xx,
                    state[1] + xx,
                    state[2] - yy,
                    state[3] + yy,
                    (state[4] + 1) % 2 )
                
                # 체크할 사항: 동작(x, y)이 가능한 동작인지 체크한다.
                # 체크 1: 보트에 승선 가능한 인원은 1~2명이다.
                # 체크 2: 승선하고 남은 인원수가 음수가 나올 수 없다. 
                # 체크 3: 이 동작을 취할 경우에 불미스러운 상황이 발생하는지 체크한다.

                # TODO .......
                # TODO .......
                # TODO .......
                # TODO .......
                
                # 체크를 하나라도 통과하지 못하면, 다른 동작으로 continue
                # 모든 체크들을 통과한 경우에 한해, 동작을 리스트에 추가한다.               
                acts.append( (action, nextState) ) 
        #print ( acts )
        return acts

    def result(self, state, action):
        #nextState = 보트문제의전이모형(state, action) 
        nextState = action[1]
        return nextState

    def goal_test(self, state):
        if ( state[0] ==  0
                and state[1] == self.initial[0]
                and state[2] ==  0
                and state[3] == self.initial[2]
                and state[4] ==1 ) : 
            return True 
        return False

    def h(self, node): 
        state=node.state 
        return state[0]   # 출발지에 남은 선교사의 수를 남은 탐색비용의 추정치로 보는 휴리스틱이다.  


def experiment():
    global MaxN, MaxP
    for n in range(1, 101):
        initial_state = [n, 0, n, 0, 0]
        print ("inital state: ", tuple(initial_state))

        p = BoatProblem(initial_state)

        sol = breadth_first_graph_search(p)
        #sol = uniform_cost_search(p)
        #sol = iterative_deepening_search(p)
        #sol = astar_search(p, p.h)
            

        if (sol) :
            print ("해법: ")
            for a in sol.solution():
                print (a)
            print("단계수: ", sol.depth)
        else : print("해법이 없음!!!")


if __name__ == "__main__" :
    initState = [3, 0, 3, 0, 0]
    print ("상태표현의 의미: ( 출발지선교사수, 도착지선교사수, 출발지식인종수, 도착지식인종수, 보트의위치)")
    print ("시작상태: ", tuple(initState))

    p = BoatProblem(initState)

    sol = breadth_first_tree_search(p)
    #sol = breadth_first_graph_search(p)
    #sol = depth_first_tree_search(p)
    #sol = depth_first_graph_search(p)

    #sol = depth_limited_search(p, 20)
    #sol = uniform_cost_search(p)
    #sol = iterative_deepening_search(p)

    #sol = astar_search(p, p.h)

    print ("해법:")
    actionPlan = sol.solution()
    for a in actionPlan :
        print(a)
    print("단계수: ", sol.depth)

#    experiment()
