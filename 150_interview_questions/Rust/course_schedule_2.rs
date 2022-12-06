// Problem Statement: There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

//     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

// Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
pub struct Graph {
    nodes: HashMap<i32, Vec<i32>>,
}

impl Graph {
    pub fn new() -> Self {
        let nodes = HashMap::new();
        return Graph{nodes}
    }
}

use std::collections::HashMap;
use std::collections::VecDeque;
impl Solution {
    // Solution Performanec: Runtime 6 ms Beats 36.84% Memory 2.5 MB Beats 78.95%
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let mut graph = Graph::new(); 
        let mut topo = HashMap::new();
        for i in 0..num_courses {
            topo.insert(i, 0);
            graph.nodes.insert(i, vec![]);
        }
        for preq in prerequisites.into_iter() {
            let dependent = preq[0];
            let course = preq[1];
            graph.nodes.get_mut(&course).unwrap().push(dependent);
            }
            
        for (_, children) in graph.nodes.iter() {
            for child in children {
                *topo.get_mut(&child).unwrap() += 1;
            }
        }

        let mut queue = VecDeque::new();
        let mut res = vec![];
        for (node, parent_count) in topo.iter() {
            if *parent_count == 0 {
                queue.push_back(*node);
            }
        }
        while queue.len() > 0 {
            let node = queue.pop_front().unwrap();
            res.push(node);
            let children = graph.nodes.get(&node).unwrap();
            for child in children.iter() {
                *topo.get_mut(child).unwrap() -= 1;
                if *topo.get_mut(child).unwrap() == 0 {
                    queue.push_back(*child);
                }
            }
        } 
        if res.len() as i32 >= num_courses {
            return res
        }
        return vec![]
        }
}