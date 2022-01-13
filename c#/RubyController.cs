using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RubyController : MonoBehaviour
{
    Rigidbody2D rigidbody2d;
    float horizontal;
    float vertical;

    // Start is called before the first frame update
    void Start()
    {
      rigidbody2d = GetComponent<Rigidbody2D>();
    }

    // Update is called once per frame
    void Update()
    {
      //setting variables for horizontal and vertical movement
      horizontal = Input.GetAxis("Horizontal");
      vertical = Input.GetAxis("Vertical");
    }

    void FixedUpdate() 
    {
      //Vector2 data type stores x and y coordinates (2d object; No Z-value needed)
      Vector2 position = rigidbody2d.position;

      //handling movement for x and y coordinates
      position.x = position.x + 3.0f * horizontal * Time.deltaTime;
      position.y = position.y + 3.0f * vertical * Time.deltaTime;

      rigidbody2d.MovePosition(position);  
    }
}
