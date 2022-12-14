# LP Addition
# Table is outputted based on manual inputs. I followed the original Tousi code workflow:
# 1. export CSV
# 2. use =IF(AND(B2>0.8,C2>0.7,B2<=F2,C2<=G2),1,0) to find criteria
#  Criteria: TPR Test>80%, TNR Test> 70%, TPR Train >= TPR Test, TNR Train > TNR Test.
# 3. Sort Values to include the greatest test and train data.
#  Sorting by Test TPR was given in example but did not always result in the correct (replicate) values
#  I used the sum of all four scores: =SUM(F2,G2,C2,B2)

# Parameter 1 is either C (SVM, LR, KLR) or alpha (RC, KRC)
# Parameter 2 is either gamma (SVM) or heuristic weight (LR, RC, KLR, KRC)
from tabulate import tabulate

data = [[1, 'SVM_1_FIS', 3.301,'1.001-5','2.901-3.401',50.001,'45.001-55','49.401-52.701',0.93, 0.93, 0.88,0.88,'none'],
        [2,'SVM_1_FES',40, '35-45','39.4-37',3.3, '1-5','3.3-3.5',0.92, 0.92, 0.83, 0.83,'none'],
        [3, 'LR_1_FIS',77.50, '70.001-80','74.201-79.901',2.2, '1.001-5','2.3',0.82, 0.81, 0.78, 0.78,'off by 0.1 for wH'],
        [4, 'LR_1_FES',30, 25-34.9,'28.7-30.2',1.8, '0.1-4.9',1.8,0.83, 0.83, 0.73,0.73,'none'],
        [5, 'KLR_1_FIS',84,'80-84.9','83.8-84.9',1.7,'1-3.9',1.7,0.88,0.88,0.73,0.73,'none'],
        [6, 'KLR_1_FES',12.701, '5.001-19.901',12.701,1.7, '1-3.9',1.7,0.88, 0.88, 0.78, 0.78,'Not in 0.001 format, 0.001 did not work'],
        [7, 'RC_1_FIS',0.801, 'P1_Calc_Range',0.601,2.5, 'P2_Calc_Range',2.7,0.76, 0.76, 0.73, 0.73,'Values do not match'],
        [8, 'RC_1_FES',4, '1-10',3.6,2.6, '1-10',2.6,0.79, 0.79, 0.73, 0.78,'Values did not match'],
        [9, 'KRC_1_FIS',0.001, 0.001-10,0.001,1.5, 1-10,1.6,91, 90, 83, 83,'Values did not match'],
        [10, 'KRC_1_FES',0.001,'0.001-9.901',0.001,2.7, '1-9.9',2.7,0.83, 0.83, 0.78, 0.78,'none'],
        [11, 'LR_126_FIS',11.301, '5.01-14.901','11.3-14.901',15.7, '5-19.9','15.7-16.3',1,1,0.86,0.86,'none'],
        [12, 'LR_126_FES',1,'1-2.9',1,15.3, '12-17.9',15.3,1, 'Test_TPR_Calc',0.86, 'Test_TNR_Calc','none'],
        [13, 'SVM_126_FIS',0.601, '0.001-4.901','0.301-0.801',5.301, '0.001-7.901','4.901-7.901',1,1,0.96,0.96,'none'],
        [14, 'SVM_126_FES',0.301, '0.001-4.901','0.301-0.401',5.501, '0.001-7.901','4.801-5.601',1,1, '0.92',0.90],'P2 odd, possible typo, train is 0.925?',
        [15, 'RC_126_FIS',0.501, '0.001-2.901',0.501,12.7, '1.1-13.9',12.7,1, 1, 0.86, 0.86,'None'],
        [16, 'RC_126_FES',6.901, '0.001-7.901','6.801-7.901',15.5, '5-16.9','15.2-15.6',1,1,0.84,0.84,'none']]
print (tabulate(data, headers=['Model',
                               'P1_Known', 'P1_Calc_Range','P1_Calc',
                               'P2_Known', 'P2_Calc_Range','P2_Calc',
                               'Test_TPR_Known', 'Test_TPR_Calc', 'Test_TNR_Known', 'Test_TNR_Calc', 'Notes']))
