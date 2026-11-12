/*
 * SPDX-FileCopyrightText: The LineageOS Project
 * SPDX-License-Identifier: Apache-2.0
 */

#include <processgroup/sched_policy.h>

// get_cpuset_policy() was removed from libprocessgroup, map it to
// get_sched_policy() which reports the policy from the same task profiles.
extern "C" int get_cpuset_policy(int tid, SchedPolicy* policy) {
    return get_sched_policy(tid, policy);
}
