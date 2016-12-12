#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def insert2Stack(self, list):
        stack = []
        while list:
            stack.append(list.val)
            list = list.next
        return stack
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = self.insert2Stack(l1)
        stack2 = self.insert2Stack(l2)
        sum = 0
        head = ListNode(0)
        
        while stack1 or stack2:
            sum += stack1.pop() if stack1 else 0
            sum += stack2.pop() if stack2 else 0
            head.val = sum % 10
            newNode = ListNode(sum/10)
            newNode.next = head
            head = newNode
            sum = sum/10
        if head.val == 0:
            head = head.next
        return head