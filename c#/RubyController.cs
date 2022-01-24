using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RubyController : MonoBehaviour
{
  public float speed = 3.0f;

  public int maxHealth = 5;
  public float timeInvincible = 2.0f;

  public int health { get { return currentHealth; }}
  int currentHealth;

  bool isInvincible;
  float invincibleTimer;

  Rigidbody2D rigidbody2d;
  float horizontal;
  float vertical;

  // Start is called before the first frame update
  void Start()
  {
    rigidbody2d = GetComponent<Rigidbody2D>();

    currentHealth = maxHealth;
  }

  // Update is called once per frame
  void Update()
  {
    //setting variables for horizontal and vertical movement
    horizontal = Input.GetAxis("Horizontal");
    vertical = Input.GetAxis("Vertical");

    if (isInvincible)
    {
      invincibleTimer -= Time.deltaTime;
      if (invincibleTimer < 0)
        isInvincible = false;
    }
  }

  void FixedUpdate() 
  {
    //Vector2 data type stores x and y coordinates (2d object; No Z-value needed)
    Vector2 position = rigidbody2d.position;

    //handling movement for x and y coordinates
    position.x = position.x + speed * horizontal * Time.deltaTime;
    position.y = position.y + speed * vertical * Time.deltaTime;

    rigidbody2d.MovePosition(position);  
  }

  public void ChangeHealth(int amount)
  {
    if (amount < 0)
    {
      if (isInvincible)
        return;
      
      isInvincible = true;
      invincibleTimer = timeInvincible;
    }

    currentHealth = Mathf.Clamp(currentHealth + amount, 0, maxHealth);
    Debug.Log(currentHealth + "/" + maxHealth);
  }
}
