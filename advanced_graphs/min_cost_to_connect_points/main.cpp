/*
https://neetcode.io/problems/min-cost-to-connect-points/question?list=neetcode150
You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.

*/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <tuple>
#include <sstream>

using namespace std;

class Solution {
public:

    // Keys are comma delimitted coordinates
    unordered_map<string, vector<tuple<int,int>>> create_adj_list(vector<vector<int>> &points) {
        unordered_map<string, vector<tuple<int,int>>> map;

        // For each individual point
        for (int i = 0; i < points.size(); i++) {
            auto point = points[i];

            ostringstream ss;
            ss << point[0] << "," << point[1];
            auto key = ss.str();

            // key not in map
            if (map.find(key) == map.end()) {
                map[key] = {};
            }

            // iterate through all other points
            for (int j = 0; j < points.size(); j++) {
                // Skip current point for key
                if (i == j) {
                    continue;
                }

                map[key].push_back(make_tuple(points[j][0], points[j][1]));

                ostringstream ss;
                ss << points[j][0] << "," << points[j][1];
                auto j_key = ss.str();

                // j_key not in map
                if (map.find(j_key) == map.end()) {
                    map[j_key] = {};
                }

                map[j_key].push_back(make_tuple(point[0], point[1]));
            }
         }

        // Print using structured bindings (C++17)
        for (const auto& [key, value] : map) {
            cout << key << " = ";

            cout << "[";
            for (int i = 0; i < value.size(); i++) {
                auto tup = value[i];
                cout << "(" << get<0>(tup) << "," << get<1>(tup) << "),";
            }
            cout << "]\n";

            cout << "\n";
        }

        return map;
    }
    
    int minCostConnectPoints(vector<vector<int>>& points) {
        auto adj_list = create_adj_list(points);
        return 0;
    }
};

int main() {
    vector<vector<int>> points = {
        {0,0},
        {2,2}
    };

    auto sol = Solution();
    sol.minCostConnectPoints(points);
}
