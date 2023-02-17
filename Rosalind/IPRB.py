# had to steal Jason Kim's solution because I was stuck on this one

# Copyright 2019 Jason Kim. All rights reserved.
# IPRB.py
# My solution to IPRB of the Rosalind Project.
# Jason Kim
# 7/24/2019
import math

# Helper function for calculating binomial coefficient
def ncr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


def dominant_probability(k, m, n):
    # Constants for probability in simple Mendelian inheritance
    # HD = homozygous dominant
    # HZ = heterozygous
    # HR = homozygous recessive
    HD_HD = 1
    HZ_HZ = 0.75
    HR_HR = 0
    HD_HZ = 1
    HZ_HR = 0.5
    HD_HR = 1
    # Parse file to get # of individuals per genotype
    #file = open("rosalind_iprb.txt", "r")
    #params = file.readline().split(' ')
    num_HD = int(k)
    num_HZ = int(m)
    num_HR = int(n)
    #file.close()
    # Compute nCr(total # of individuals, 2)
    total_pairs = ncr(num_HD + num_HZ + num_HR, 2)
    # Then calculate probability of each genotype pair to mate
    pr_HD_HD = ncr(num_HD, 2) / total_pairs
    pr_HZ_HZ = ncr(num_HZ, 2) / total_pairs
    pr_HR_HR = ncr(num_HR, 2) / total_pairs
    pr_HD_HZ = (num_HD * num_HZ) / total_pairs
    pr_HZ_HR = (num_HZ * num_HR) / total_pairs
    pr_HD_HR = (num_HD * num_HR) / total_pairs
    # Compute Pr(genotype pair mating) *
    # Pr(offspring of that pair having A) and sum
    total = 0.0
    total += (pr_HD_HD * HD_HD)
    total += (pr_HZ_HZ * HZ_HZ)
    total += (pr_HR_HR * HR_HR)
    total += (pr_HD_HZ * HD_HZ)
    total += (pr_HZ_HR * HZ_HR)
    total += (pr_HD_HR * HD_HR)
    print(round(total, 5))
    return

print(dominant_probability(26,25,21))



# my attempts at a solution

def dominant_probability(k, m, n):
    total = k + m + n
    # probability of selecting a homozygous dominant individual
    prob_hom_dom = k / total
    # probability of selecting a heterozygous individual
    prob_het = m / total
    # probability of selecting a homozygous recessive individual
    prob_hom_rec = n / total
    # probability of producing an individual with a dominant allele
    # P(dom) = P(hom dom x any) + P(het x hom dom) + P(hom rec x hom dom) + P(het x het x 0.75)
    # hom dom x hom dom (x2) = 1
    # het x het (x2) = 0.75
    # hom dom x het = 1
    # het x hom dom = 1
    # hom dom x hom rec = 1
    # hom rec x hom dom = 1
    # het x hom rec = 0.5
    # hom rec x het = 0.5
    #print(2 * (prob_hom_dom * ((k - 1) / (total - 1))))
    #print(2 * (prob_het * ((m - 1) / (total - 1)) * 0.75))
    #print(prob_hom_dom * ((m) / (total - 1)))
    #print(prob_het * ((k) / (total - 1)))
    #print(prob_hom_dom * ((n) / (total - 1)))
    #print(prob_hom_rec * ((k) / (total - 1)))
    #print(prob_het * ((n) / (total - 1)) * 0.5)
    #print(prob_hom_rec * ((m) / (total - 1)) * 0.5)
    prob_dom = 2 * (prob_hom_dom * ((k - 1) / (total - 1))) + \
                2 * (prob_het * ((m - 1) / (total - 1)) * 0.75) + \
                prob_hom_dom * ((m) / (total - 1)) + \
                prob_het * ((k) / (total - 1)) + \
                prob_hom_dom * ((n) / (total - 1)) + \
                prob_hom_rec * ((k) / (total - 1)) + \
                prob_het * ((n) / (total - 1)) * 0.5 + \
                prob_hom_rec * ((m) / (total - 1)) * 0.5 + \
                    2 * (prob_hom_rec * ((n - 1) / (total - 1))) + \
                    prob_hom_rec * ((m) / (total - 1)) * 0.5 + \
                    prob_het * ((n) / (total - 1)) * 0.5 + \
                    2 * (prob_het * ((m - 1) / (total - 1)) * 0.25)
                
    return prob_dom


def dominant_probability(k, m, n):
    total = k + m + n
    # probability of selecting homozygous dominant organism
    p_k = k / total
    # probability of selecting heterozygous organism
    p_m = m / total
    # probability of selecting homozygous recessive organism
    p_n = n / total
    # probability of selecting two homozygous dominant organisms
    p_kk = p_k * (k - 1) / (total - 1)
    # probability of selecting two heterozygous organisms
    p_mm = p_m * (m - 1) / (total - 1)
    # probability of selecting two homozygous recessive organisms
    p_nn = p_n * (n - 1) / (total - 1)
    # probability of selecting one homozygous dominant and one heterozygous organism
    p_km = p_k * p_m * 2 / (total - 1)
    p_mk = p_m * p_k * 2 / (total - 1)
    # probability of selecting one homozygous dominant and one homozygous recessive organism
    p_kn = p_k * p_n * 2 / (total - 1)
    p_nk = p_n * p_k * 2 / (total - 1)
    # probability of selecting one heterozygous and one homozygous recessive organism
    p_mn = p_m * p_n * 2 / (total - 1)
    p_nm = p_n * p_m * 2 / (total - 1)
    # probability of producing an individual with dominant phenotype
    p_dominant = 1 - 2 * p_nn - 2 * p_mm * 0.25 - p_mn * 0.5 - p_nm * 0.5
    return p_dominant