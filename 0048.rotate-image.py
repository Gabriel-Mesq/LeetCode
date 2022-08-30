#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i):

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
        
# @lc code=end

