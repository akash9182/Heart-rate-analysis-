package nodomain.freeyourgadget.gadgetbridge.service.btle.profiles.heartrate;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.EditText;

import nodomain.freeyourgadget.gadgetbridge.R;


public class RemoveFrustration extends AppCompatActivity {
//    private static final Logger LOG = LoggerFactory.getLogger(AlarmReceiver.class);

//    private Handler handler;
//    public int timeRemaining = 60;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EditText text = (EditText) findViewById(R.id.Edit);
//        final TextView label = (TextView) findViewById(R.id.counter);
//        label.setText(Integer.toString(timeRemaining));
//        final Button done = (Button) findViewById(R.id.done);
        setContentView(R.layout.activity_remove_frustration);
//
//        done.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                Intent i = new Intent(RemoveFrustration.this, DebugActivity.class);
//                startActivity(i);
////                finish();
//            }
//        });

//        handler = new Handler();
//
//        Runnable runnable = new Runnable() {
//            @Override
//            public void run() {
//                timeRemaining = timeRemaining - 1;
//                label.setText(Integer.toString(timeRemaining));
//                if (timeRemaining < 0) {
//                    handler.postDelayed(this, 1000);
//                    LOG.info("I am here");
//                }
//            }
//        };

//        handler.postDelayed(runnable,1000);
    }


}
