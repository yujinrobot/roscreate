/**
 * @file /include/%(name)s/%(name)s.hpp
 *
 * @brief Template class for %(name)s.
 **/
#ifndef %(name)s_HPP
#define %(name)s_HPP

/*****************************************************************************
 ** Includes
 *****************************************************************************/

#include <ros/ros.h>

/*****************************************************************************
 ** Namespace
 *****************************************************************************/

namespace %(name)s
{
  /**
   * @brief Template class for $(name)s
   */
  class Foo
  {

  public:
    Foo() {};

    void helloDude();
  };

} // namespace %(name)s

#endif // %(name)s_HPP
