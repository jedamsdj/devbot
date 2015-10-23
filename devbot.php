<?php
	$incoming_number = $_REQUEST['From'];
	$incoming_text   = $_REQUEST['Body'];

    if (empty($incoming_number)) {
        $text = 'Nothing to see here. Move along now.'
    } else {
	    $text = exec('timeout 1 python /Users/Devon/Documents/Coding/devbot/receive_texts_twilio.py ' . $incoming_number . ' ' . $incoming_text);
	    if (empty($text)) {
		    $text = 'Looks like something is wrong, try again in a few minutes.';
	    }
    }

	header('content-type: text/xml');
	echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
?>

<Response>
	<Message><?php echo $text ?></Message>
</Response>